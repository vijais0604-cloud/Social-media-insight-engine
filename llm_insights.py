import os
from openai import OpenAI
from dotenv import load_dotenv
from database import get_db_connection

load_dotenv()
client = OpenAI() # Picks up OPENAI_API_KEY from .env

def check_for_crisis(cur):
    # Get negative count from the last 6 hours vs previous 6 hours
    cur.execute("""
        SELECT 
            COUNT(*) FILTER (WHERE created_at > now() - interval '6 hours') as current_period,
            COUNT(*) FILTER (WHERE created_at BETWEEN now() - interval '12 hours' AND now() - interval '6 hours') as previous_period
        FROM tweets 
        WHERE sentiment_label = 'Negative'
    """)
    current, previous = cur.fetchone()
    
    # Calculate % increase
    if previous > 0:
        increase = ((current - previous) / previous) * 100
    else:
        increase = 0

    return {
        "is_crisis": increase > 300, # Threshold for 340% spike
        "increase": f"{int(increase)}%",
        "count": current
    }
def get_llm_summary(query, tweets):
    if not tweets:
        return "No data found for this query."
    
    # Combine tweets into one text block for the LLM
    context = "\n".join(tweets[:50]) # Use top 50 for token limits
    
    prompt = f"""
    Analyze these social media posts about '{query}':
    {context}
    
    Provide a concise summary including:
    1. Overall sentiment.
    2. Main topics mentioned.
    3. Brand dominance/perception.
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content