import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


try:
    conn = psycopg2.connect(os.getenv("POSTGRES_URL"))
    print("Connected successfully!")

    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    print(cursor.fetchone())  # Output PostgreSQL version

    conn.close()
except psycopg2.Error as e:
    print(f"Database connection error: {e}")
