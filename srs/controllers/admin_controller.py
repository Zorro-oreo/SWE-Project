from flask import Blueprint, render_template, request, session
from srs.repositories.adminRepo import adminRepo
from srs.db import get_db

admin_bp = Blueprint("admin", __name__)

@admin_bp.route('/ManageUsers')
def manage():

    return render_template("ManageUsers.html")

@admin_bp.route("/AddUser", methods=["POST"])
def addUser():

    type = request.form["usertype"]
    id = request.form["id"]
    name = request.form["name"]
    password = request.form["password"]
    
    db = get_db()
    admin_id = session.get('userID')

    status = ""

    if (type == "Student"):

        status = adminRepo(db, admin_id).add_student(id, name, password)

    elif (type == "Professor"):

        status = adminRepo(db, admin_id).add_prof(id, name, password)

    elif (type == "Admin"):

        status = adminRepo(db, admin_id).add_admin(id, name, password)

    return render_template("ManageUsers.html", message = status)

@admin_bp.route('/ManageCourses')
def manage_courses():
    return render_template("ManageCourses.html")


@admin_bp.route("/AddCourse", methods=["POST"])
def addCourse():
    c_id = request.form["course_id"]
    cname = request.form["course_name"]
    capacity = request.form["capacity"]
    professor_id = request.form["professor_id"]

    db = get_db()
    admin_id = session.get('userID')

    status = adminRepo(db, admin_id).add_course(c_id, cname, capacity, professor_id)

    return render_template("ManageCourses.html", message=status)


@admin_bp.route("/RemoveCourse", methods=["POST"])
def removeCourse():
    c_id = request.form["course_id"]

    db = get_db()
    admin_id = session.get('userID')

    status = adminRepo(db, admin_id).remove_course(c_id)

    return render_template("ManageCourses.html", message=status)
