document.addEventListener('DOMContentLoaded', function () {

    /* =========================
       1. Sentiment Chart
    ========================== */
    
    const ctx = document.getElementById('sentimentChart').getContext('2d');

    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Positive', 'Neutral', 'Negative'],
            datasets: [{
                data: [
                    SENTIMENT_BREAKDOWN.Positive || 0,
                    SENTIMENT_BREAKDOWN.Neutral || 0,
                    SENTIMENT_BREAKDOWN.Negative || 0
                ],
                backgroundColor: ['#198754', '#6c757d', '#dc3545']
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    });

    /* =========================
       2. Fetch Trends (<2s load)
    ========================== */
    fetch('/trends')
        .then(res => res.json())
        .then(data => {
            const list = document.getElementById('trend-list');
            list.innerHTML = data.map(t => `
                <div class="list-group-item d-flex justify-content-between align-items-center">
                    #${t.topic}
                    <span class="badge bg-primary rounded-pill">${t.count}</span>
                </div>
            `).join('');
        })
        .catch(err => console.error('Trend fetch failed', err));

    /* =========================
       3. Crisis Detection
    ========================== */
    fetch('/crisis-check')
        .then(res => res.json())
        .then(data => {
            if (data.status === "Alert") {
                document.getElementById('crisis-text').innerHTML = `
                    <strong>${data.increase}% increase</strong> in negative sentiment detected.<br>
                    <em>Keywords: ${data.keywords.join(', ')}</em>
                `;
            } else {
                document.getElementById('crisis-text').textContent =
                    "No abnormal sentiment spikes detected.";
            }
        })
        .catch(err => console.error('Crisis check failed', err));
});