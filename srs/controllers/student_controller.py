from flask import Flask, render_template, session, request, flash, redirect, Blueprint
from flask_login import login_required, current_user
from srs.models.student import Student
from srs.repositories.studentRepo import studentRepo
from srs.db import get_db
import sqlite3

student_bp = Blueprint('student', __name__)

@student_bp.route('/view_grades')
@login_required
def view_grades():
    student_id = current_user.sID
    if not student_id:
        return "Not logged in"
    
    db = get_db()
    
    repo = studentRepo(db, student_id)
    grades = repo.get_grades()
    gpa = current_user.get_GPA(grades)

    return render_template('view_grades.html', gpa=gpa, grades=grades)

@student_bp.route('/course_reg')
@login_required
def course_reg():

    student_id = current_user.sID

    db = get_db()
    
    courses = studentRepo(db, student_id).getAvailableCourses()

    return render_template("register_course.html", courses = courses)

@student_bp.route('/register_course', methods=['POST'])
@login_required
def register_course():

    course_id = request.form.get("course_id")
    student_id = current_user.sID

    db = get_db()

    try:
        studentRepo(db, student_id).RegisterCourse(course_id)
        return f"""
            <p>You have registered for course: {course_id}</p>
            <a href='/StudentHome'>Click here to go back to Student Home</a>
        """
    except sqlite3.IntegrityError:
        return f"""
            <h1>Error</h1>
            <p>You are already registered for this course.</p>
        """
    except Exception as e:
        return f"""
            <h1>Error</h1>
            <p>{str(e)}</p>
            <a href='/StudentHome'>Click here to go back</a>
        """

@student_bp.route('/drop_course', methods=['GET', 'POST'])
@login_required
def drop_course():
    student_id = current_user.sID
    if not student_id:
        return "Not logged in"

    if request.method == 'POST':
        course_id = request.form.get("course_id")
        db = get_db()
        try:
            studentRepo(db, student_id).DropCourse(course_id)
            return f"""
                <p>You have dropped course: {course_id}</p>
                <a href='/StudentHome'>Click here to go back to Student Home</a>
            """
        except Exception as e:
            return f"""
                <h1>Error</h1>
                <p>{str(e)}</p>
                <a href='/StudentHome'>Click here to go back</a>
            """
    else:
        return render_template("drop_course.html")
    
@student_bp.route('/StudentRegisteredCourses')
@login_required
def student_registered_courses():
    student_id = current_user.sID
    if not student_id:
        return "Not logged in"

    db = get_db()
    
    registered_courses = studentRepo(db, student_id).get_registered_courses()

    return render_template("StudentRegisteredCourses.html", registered_courses=registered_courses)