import psycopg2
import pandas as pd
from io import StringIO

def fast_ingest():
    # 1. Load data with Pandas (assuming Sentiment140 format)
    # 0=target, 1=id, 2=date, 3=flag, 4=user, 5=text
    cols = ['sentiment', 'id', 'date', 'query', 'user', 'content']
    df = pd.read_csv('/Users/vijais/Documents/vs code/social_media_insight_engine/data/sentiment140.csv', 
                     encoding='latin-1', names=cols)
    
    # Take a sample of 500k to meet requirements
    df = df.sample(n=500000)

    # Convert sentiment: 0 -> 'Negative', 4 -> 'Positive'
    df['sentiment_label'] = df['sentiment'].map({0: 'Negative', 4: 'Positive'})

    # 2. Prepare for PostgreSQL
    conn = psycopg2.connect(dbname="sentimentdb", user="vijais")
    cur = conn.cursor()
    
    import csv # Add this at the top of your file

 # ... inside your fast_ingest function ...

    buffer = StringIO()
   # Use quoting=csv.QUOTE_ALL to ensure commas inside tweets don't break the COPY
    df[['sentiment_label', 'content']].to_csv(
    buffer, 
    index=False, 
    header=False, 
    quoting=csv.QUOTE_ALL, 
    sep=','
 )
    buffer.seek(0)

# Use copy_expert instead of copy_from to handle the CSV formatting
    sql = """
    COPY tweets (sentiment_label, content) 
    FROM STDIN WITH (FORMAT CSV, QUOTE '"', DELIMITER ',')
   """
    cur.copy_expert(sql, buffer)
   
    
    conn.commit()
    print("✅ Analyzed and loaded 500,000 posts in seconds.")
    cur.close()
    conn.close()

if __name__ == "__main__":
    fast_ingest()