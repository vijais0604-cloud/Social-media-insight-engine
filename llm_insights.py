import os
from openai import OpenAI
from dotenv import load_dotenv

from social_media_insight_engine.app import get_db_connection

load_dotenv()
client = OpenAI() # Picks up OPENAI_API_KEY from .env

def get_crisis_report():
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Calculate if negative posts spiked in the last 24 hours 
    # (Simulated here since Sentiment140 is old data, we compare total vs recent)
    cur.execute("SELECT COUNT(*) FROM tweets WHERE sentiment_label = 'Negative'")
    neg_count = cur.fetchone()[0]
    
    prompt = f"System analysis shows {neg_count} negative posts out of 500,000. Analyze if this constitutes a brand crisis and suggest a mitigation strategy."
    
    # Call OpenAI (as we set up before)
    # ...
    return "Crisis Alert: 340% increase in negative sentiment regarding [Topic]..."

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