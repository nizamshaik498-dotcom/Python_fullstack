import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='nizam07',
            database='school_db')

        if conn.is_connected(): 
            print("✅ Connected to MySQL successfully")
            return conn
    except Error as e:
        print(f"❌ Connection failed: {e}")
        return None

get_connection()