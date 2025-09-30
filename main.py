import psycopg
from pgvector.psycopg import register_vector
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

HTML_DIR = "pages"


def get_db_connection():
    """Creates a connection to PostgreSQL with vector support."""
    conn = psycopg.connect(
        host="localhost",
        dbname="postgres",
        user="postgres",
        password="postgres",
        port=5432
    )
    register_vector(conn)
    return conn


def parse_html_to_text(html_path):
    """Extracts clean text content from HTML file."""
    with open(html_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        body = soup.body
        if body:
            return body.get_text(separator='\n', strip=True)
        return ""


def ingest():
    """Reads Notion pages and stores them with embeddings in the database."""
    conn = get_db_connection()
    cur = conn.cursor()

    html_files = [f for f in os.listdir(HTML_DIR) if f.endswith('.html')]

    for index, html_file in enumerate(html_files, 1):
        print(f"Processing {index}/{len(html_files)}: {html_file}")

        html_path = os.path.join(HTML_DIR, html_file)
        text = parse_html_to_text(html_path)

        if text:
            # TODO: Generate embedding vector for the page content
            raise NotImplementedError("not implemented")

    conn.commit()
    cur.close()
    conn.close()
    print(f"✅ Ingested {len(html_files)} pages")


def retrieve_similar_content(query_text, limit=3):
    """Finds pages most similar to the query using vector search."""
    # TODO: Convert query to embedding
    # TODO: Find similar embeddings using cosine distance

    raise NotImplementedError("not implemented")


def generate_response(query, relevant_contexts):
    """Generates AI answer based on relevant page content."""
    raise NotImplementedError("not implemented")


if __name__ == "__main__":
    # Step 1: Ingest Notion pages (comment this out after first run)
    ingest()

    # Step 2: Query the knowledge base
    query = "What is our organization email?"
    similar_pages = retrieve_similar_content(query, limit=3)
    response = generate_response(query, similar_pages)

    print(f"\nQuery: {query}")
    print(f"\nAnswer:\n{response}")
