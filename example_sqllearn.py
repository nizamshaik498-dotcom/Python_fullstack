import mysql.connector
from mysql.connector import Error

class SchoolDatabase:
    def __init__(self):
        self.config = {
            "host": "localhost",
            "user": "root",
            "password": "nizam07",
            "database": "school_db"
        }
        # Verify connection on startup
        try:
            conn = self.get_connection()
            if conn.is_connected():
                print("✅ MySQL connected successfully!")
                conn.close()
                self.init_table()
        except Error as e:
            print(f"❌ Connection failed: {e}")
            exit()

    def get_connection(self):
        return mysql.connector.connect(**self.config)

    def init_table(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100),
                department VARCHAR(50),
                marks FLOAT
            )
        """)
        conn.commit()
        cursor.close()
        conn.close()

    def add_student(self, name, department, marks):
        conn = self.get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO students (name, department, marks) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, department, marks))
        conn.commit()
        print(f"✅ Added student: {name} (ID: {cursor.lastrowid})")
        cursor.close()
        conn.close()

    def get_all_students(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, department, marks FROM students")
        rows = cursor.fetchall()
        print("\n--- Current Student List ---")
        for row in rows:
            print(f"ID:{row[0]} | {row[1]} | {row[2]} | {row[3]}")
        cursor.close()
        conn.close()

    def update_marks(self, student_id, new_marks):
        conn = self.get_connection()
        cursor = conn.cursor()
        query = "UPDATE students SET marks = %s WHERE id = %s"
        cursor.execute(query, (new_marks, student_id))
        conn.commit()
        print(f"✅ Updated ID {student_id} with new marks: {new_marks}")
        cursor.close()
        conn.close()

    def get_students_above(self, min_marks):
        conn = self.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT name, department, marks FROM students WHERE marks >= %s ORDER BY marks DESC",
            (min_marks,)
        )
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    db = SchoolDatabase()

    db.add_student("Priya", "CS", 88.50)
    db.get_all_students()
    db.update_marks(1, 92.00)
    db.get_all_students()
    
    print("\n--- Students scoring above 75 ---")
    high_scorers = db.get_students_above(75)
    for s in high_scorers:
        print(f"{s['name']:15} {s['department']:8} {s['marks']}")