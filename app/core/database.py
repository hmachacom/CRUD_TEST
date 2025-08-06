"""
This module handles the database connection and provides a cursor for database operations.
It uses psycopg2 to connect to a PostgreSQL database, with connection details
loaded from the application's configuration.
"""
import psycopg2
from psycopg2.extras import RealDictCursor
from core.config import config


def get_connection():
    return psycopg2.connect(
        host=config.DB_HOST,
        port=config.DB_PORT,
        dbname=config.DB_NAME,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        cursor_factory=RealDictCursor)

    
def execute_query(query, params=None, fetch=False):
    conn = get_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursor.execute(query, params)
        if fetch:
            data = cursor.fetchall()
        else:
            data = None
        conn.commit()
        return data
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()


def test_connection():
    try:
        conn = psycopg2.connect(
            host=config.DB_HOST,
            port=config.DB_PORT,
            dbname=config.DB_NAME,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
        )
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()
        print("✅ Conexión exitosa a PostgreSQL:", version)
        cur.close()
        conn.close()
    except Exception as e:
        print("❌ Error de conexión a la base de datos:", e)
