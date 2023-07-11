from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Initialize the SQLite database
def init_db():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER, gender TEXT)")
    conn.commit()
    conn.close()

# Home page - List all students
@app.route('/')
def index():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    return render_template('index.html', students=students)

# Add student form
@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name, age, gender) VALUES (?, ?, ?)", (name, age, gender))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('add.html')

# Edit student
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']

        cursor.execute("UPDATE students SET name=?, age=?, gender=? WHERE id=?", (name, age, gender, id))
        conn.commit()
        conn.close()
        return redirect('/')

    cursor.execute("SELECT * FROM students WHERE id=?", (id,))
    student = cursor.fetchone()
    conn.close()
    return render_template('edit.html', student_id=id, student=student)

# Delete student
@app.route('/delete/<int:id>', methods=['POST'])
def delete_student(id):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
