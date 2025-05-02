import psycopg2
import os

def create_db_tables():
    # Get the DATABASE_URL from the environment
    database_url = os.getenv("DATABASE_URL")
    
    # Connect to PostgreSQL database
    conn = psycopg2.connect(database_url)
    cursor = conn.cursor()
    
    # Read the SQL file and execute it
    with open('dbCreateStatements-Postgres.txt', 'r') as f:
        sql = f.read()
        cursor.execute(sql)
        conn.commit()
    
    cursor.close()
    conn.close()

# Run the function to create tables when the app starts
create_db_tables()
