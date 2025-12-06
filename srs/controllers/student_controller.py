from flask import Flask, render_template, session, request, flash, redirect
from models.student import Student
import sqlite3

app = Flask(__name__, template_folder='../templates')

@app.route('/view_grades')
def view_grades():
    sgrades = [
        {'course': 'Mathematics', 'grade': 'A'},
        {'course': 'Science', 'grade': 'B+'},
        {'course': 'History', 'grade': 'A-'}
    ]
    return render_template('view_grades.html', grades=sgrades)

@app.route('/register_course')
def register_course():

    course_id = request.form.get("course_id")
    student_id = session["userID"]

    student = Student(student_id, "", "")
    try:
        student.RegisterCourse(course_id)
        flash("Registered successfully.")
    except sqlite3.IntegrityError:
        flash("Alreaady registered")
    except Exception as e:
        flash(f"Error: {str(e)}.")

    return redirect("/StudentHome")

if __name__ == '__main__':
    app.run(debug=True)