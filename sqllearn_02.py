
import mysql.connector 
from mysql.connector import Error

# Best practice: store connection config in one place
DB_CONFIG = { 
    "host": "localhost",
    "user": "root", 
    "password": "nizam07", # Ensure this matches your actual password
    "database": "school_db" 
}

def get_students_above(min_marks):
    """Fetch all students scoring above min_marks."""
    conn = None 
    try:
        conn = mysql.connector.connect(**DB_CONFIG) 
        cursor = conn.cursor(dictionary=True) 
        cursor.execute(
            "SELECT name, department, marks FROM students WHERE marks >= %s ORDER BY marks DESC", 
            (min_marks,) 
        )
        results = cursor.fetchall()
        cursor.close() 
        return results
    except Error as e:
        print(f"Database error: {e}")
        return [] 
    finally:
        if conn and conn.is_connected():
            conn.close() 

# Use the function
if __name__ == "__main__":
    students = get_students_above(75)
    for s in students:
        # :15 and :8 are format specifiers that add padding for alignment
        print(f"{s['name']:15} {s['department']:8} {s['marks']}")