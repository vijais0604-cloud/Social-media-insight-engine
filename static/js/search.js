async function search() {
    const query = document.getElementById('q').value;
    const output = document.getElementById('out');
    
    if (!query) return alert("Please enter a topic!");

    output.innerHTML = '<div class="spinner-border text-primary" role="status"></div> Analyzing 500k+ posts...';

    try {
        const response = await fetch(`/search?q=${encodeURIComponent(query)}`);
        const data = await response.json();
        output.innerText = data.summary;
    } catch (error) {
        output.innerText = "Error: Could not reach the sentiment engine.";
    }
}