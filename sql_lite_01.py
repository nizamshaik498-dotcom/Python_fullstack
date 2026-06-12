import sqlite3

conn = sqlite3.connect("school.db")
conn_memory = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        department TEXT,
        marks REAL
    )
""")

conn.commit()

cursor.execute(
    "INSERT INTO students (name, age, department, marks) VALUES (?, ?, ?, ?)",
    ("Priya", 20, "CS", 88.5)
)

students = [
    ("Ravi", 21, "ECE", 75.0),
    ("Meena", 20, "CS", 92.0),
    ("Arjun", 22, "MECH", 65.5),
]
cursor.executemany(
    "INSERT INTO students (name, age, department, marks) VALUES (?, ?, ?, ?)",
    students
)
conn.commit()

cursor.execute("SELECT * FROM students ORDER BY marks DESC")
all_students = cursor.fetchall()
for row in all_students:
    print(f" {row[1]:12} | {row[3]:6} | {row[4]}")

cursor.execute("SELECT name, marks FROM students WHERE marks > ?", (80,))
while True:
    row = cursor.fetchone()
    if row is None:
        break
    print(row)

conn.row_factory = sqlite3.Row
cursor2 = conn.cursor()
cursor2.execute("SELECT * FROM students")
for row in cursor2.fetchall():
    print(f"Name: {row['name']}, Marks: {row['marks']}")

cursor.execute("UPDATE students SET marks = ? WHERE name = ?", (95.0, "Priya"))
conn.commit()
print(f"Updated: {cursor.rowcount} row(s)")

cursor.execute("DELETE FROM students WHERE marks < ?", (50,))
conn.commit()

cursor.close()
conn.close()