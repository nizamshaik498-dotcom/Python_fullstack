import sqlite3

with sqlite3.connect("school.db") as conn:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, department, marks) VALUES (?,?,?)", ("Test", "CS", 70))
    cursor.execute("UPDATE students SET marks = marks + 5 WHERE department = ?", ("CS",))
    results = cursor.execute("SELECT name, marks FROM students").fetchall()
    for name, marks in results:
        print(f" {name}: {marks}")

class Database:
    def __init__(self, db_path):
        self.db_path = db_path

    def _get_conn(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def setup(self):
        with self._get_conn() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    department TEXT,
                    marks REAL
                )
            """)

    def add(self, name, department, marks):
        with self._get_conn() as conn:
            conn.execute(
                "INSERT INTO students (name, department, marks) VALUES (?,?,?)",
                (name, department, marks)
            )
            print(f"Added: {name}")

    def get_all(self):
        with self._get_conn() as conn:
            rows = conn.execute("SELECT * FROM students ORDER BY marks DESC").fetchall()
            return [dict(row) for row in rows]

db = Database("school.db")
db.setup()
db.add("Priya", "CS", 88.5)
db.add("Ravi", "ECE", 72.0)
print(db.get_all())

print("Done")