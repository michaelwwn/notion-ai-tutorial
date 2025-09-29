import psycopg
from pgvector.psycopg import register_vector
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from openai import OpenAI
from pprint import pprint

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
model = "text-embedding-3-small"

HTML_DIR = "pages"

def get_db_connection():
    conn = psycopg.connect(
        host="localhost",
        dbname="postgres",
        user="postgres",
        password="postgres",
        port=5432
    )
    register_vector(conn)
    return conn

def ingest():
    raise NotImplementedError("not implemented")

def generate_response(query, contexts):
    raise NotImplementedError("not implemented")

def retrieve(query_text, limit=3):
    raise NotImplementedError("not implemented")
    
def parse_html_to_text(html_path):
    raise NotImplementedError("not implemented")
        
if __name__ == "__main__":
    # ingest()
    
    query = "What is the escalation procedure for withdrawal failure."
    contexts = retrieve(query)
    response = generate_response(query, contexts)
    
    print(response)