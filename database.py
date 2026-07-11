import sqlite3

connection = sqlite3.connect("student.db", check_same_thread=False)
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    course TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

connection.commit()


# Add Student
def add_student(student_id, name, age, course, email):

    cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))

    if cursor.fetchone():
        return

    cursor.execute("""
    INSERT INTO students(id,name,age,course,email)
    VALUES(?,?,?,?,?)
    """, (student_id, name, age, course, email))

    connection.commit()


# View Students
def get_all_students():

    cursor.execute("SELECT * FROM students")

    return cursor.fetchall()


# =========================
# Total Students
# =========================
def get_total_students():

    cursor.execute("SELECT COUNT(*) FROM students")

    return cursor.fetchone()[0]


# Search Student
def search_student(student_id):

    cursor.execute(
        "SELECT * FROM students WHERE id=?",
        (student_id,)
    )

    return cursor.fetchone()


# Update Student
def update_student(student_id, name, age, course, email):

    cursor.execute("""
    UPDATE students
    SET name=?, age=?, course=?, email=?
    WHERE id=?
    """, (name, age, course, email, student_id))

    connection.commit()


# Delete Student
def delete_student(student_id):

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (student_id,)
    )

    connection.commit()


# Close Connection
def close_connection():
    connection.close()