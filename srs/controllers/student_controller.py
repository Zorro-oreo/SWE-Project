from flask import Flask, render_template, session, request, flash, redirect, Blueprint
from models.student import Student
import sqlite3

student_bp = Blueprint('student', __name__)

@student_bp.route('/view_grades')
def view_grades():
    sgrades = [
        {'course': 'Mathematics', 'grade': 'A'},
        {'course': 'Science', 'grade': 'B+'},
        {'course': 'History', 'grade': 'A-'}
    ]
    return render_template('view_grades.html', grades=sgrades)

@student_bp.route('/course_reg')
def course_reg():

    return render_template("register_course.html")

@student_bp.route('/register_course', methods=['POST'])
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