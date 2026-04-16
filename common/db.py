import psycopg2, os

def get_conn():
    return psycopg2.connect(
        dbname="assetdb",
        user="postgres",
        password="postgres",
        host=os.getenv("POSTGRES_HOST", "postgres")
    )
