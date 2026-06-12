import mysql.connector 
from mysql.connector import Error

def add_student(name, department, marks):
    conn = mysql.connector.connect(host="localhost", user="root", password="nizam07", database="school_db")
    cursor = conn.cursor() 
    # Removed 'age' from the query and values
    query = """ INSERT INTO students (name, department, marks) VALUES (%s, %s, %s) """ 
    values = (name, department, marks)
    cursor.execute(query, values)
    conn.commit()
    print(f"✅ Student added with ID: {cursor.lastrowid}") 
    conn.close()

def get_all_students(): 
    conn = mysql.connector.connect(host="localhost", user="root", password="nizam07", database="school_db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, department, marks FROM students")
    rows = cursor.fetchall()
    # Fixed indexing issue: added a loop to iterate through rows
    for row in rows:
        print(f"ID:{row[0]} | {row[1]} | {row[2]} | {row[3]}")
    cursor.close()
    conn.close()
    return rows 

def get_students_as_dicts():
    conn = mysql.connector.connect(host="localhost", user="root", password="nizam07", database="school_db")
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows: print(f"Name: {row['name']}, Marks: {row['marks']}")
    cursor.close()
    conn.close()

def update_marks(student_id, new_marks):
    conn = mysql.connector.connect(host="localhost", user="root", password="nizam07", database="school_db") 
    cursor = conn.cursor() 
    query = "UPDATE students SET marks = %s WHERE id = %s"
    cursor.execute(query, (new_marks, student_id))
    conn.commit()
    print(f"✅ Updated {cursor.rowcount} row(s)")
    cursor.close()
    conn.close()

def delete_student(student_id):
    conn = mysql.connector.connect(host="localhost", user="root", password="nizam07", database="school_db") 
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
    conn.commit() 
    print(f"🗑️ Deleted student with ID {student_id}")
    cursor.close()
    conn.close()

if __name__ == "__main__":
    # Updated call to match new add_student arguments
    add_student("Priya", "CS", 88.50) 
    get_all_students()
    update_marks(1, 92.00)
    get_all_students()