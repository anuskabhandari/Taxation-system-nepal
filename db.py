import psycopg2

def get_connection():
    try:
        conn = psycopg2.connect(
            user="postgres",          # your PostgreSQL username
            password="Rekha123",  # your PostgreSQL password
            host="localhost",         # usually localhost
            port="5432",              # default port
            dbname="taxdb"            # your database name
        )
        print("Database connected successfully")
        return conn

    except Exception as e:
        print("Error connecting to database:", e)
        return None