from flask import Blueprint, render_template, request, session
from flask_login import login_required, current_user
from srs.repositories.adminRepo import adminRepo
from srs.db import get_db

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

@admin_bp.route('/ManageUsers')
@login_required
def manage():

    return render_template("ManageUsers.html")

@admin_bp.route("/AddUser", methods=["POST"])
@login_required
def addUser():

    type = request.form["usertype"]
    id = request.form["id"]
    name = request.form["name"]
    password = request.form["password"]
    
    db = get_db()
    admin_id = current_user.id

    status = ""

    if (type == "Student"):

        status = adminRepo(db, admin_id).add_student(id, name, password)

    elif (type == "Professor"):

        status = adminRepo(db, admin_id).add_prof(id, name, password)

    elif (type == "Admin"):

        status = adminRepo(db, admin_id).add_admin(id, name, password)

    return render_template("ManageUsers.html", message = status)

@admin_bp.route('/ManageAccounts')
def manage_accounts():
    db = get_db()
    admin_id = session.get('userID')
    
    students = adminRepo(db, admin_id).get_all_students()
    professors = adminRepo(db, admin_id).get_all_professors()
    
    return render_template("ManageAccounts.html", 
                          students=students, 
                          professors=professors)

@admin_bp.route('/edit_student/<student_id>')
def edit_student(student_id):
    db = get_db()
    admin_id = session.get('userID')
    
    student = adminRepo(db, admin_id).get_student_by_id(student_id)
    
    if not student:
        return "Student not found"
    
    return render_template("EditStudent.html", student=student)

@admin_bp.route('/update_student/<student_id>', methods=['POST'])
def update_student(student_id):
    db = get_db()
    admin_id = session.get('userID')
    
    name = request.form.get('name')
    password = request.form.get('password')
    
    if password and password.strip():
        status = adminRepo(db, admin_id).update_student(student_id, name, password)
    else:
        status = adminRepo(db, admin_id).update_student(student_id, name)
    
    return render_template("EditStudent.html", 
                          student={'stID': student_id, 'sname': name}, 
                          message=status)

@admin_bp.route('/delete_student/<student_id>', methods=['POST'])
def delete_student(student_id):
    db = get_db()
    admin_id = session.get('userID')
    
    status = adminRepo(db, admin_id).delete_student(student_id)
    
    students = adminRepo(db, admin_id).get_all_students()
    professors = adminRepo(db, admin_id).get_all_professors()
    
    return render_template("ManageAccounts.html", 
                          students=students, 
                          professors=professors, 
                          message=status)

@admin_bp.route('/edit_professor/<professor_id>')
def edit_professor(professor_id):
    db = get_db()
    admin_id = session.get('userID')
    
    professor = adminRepo(db, admin_id).get_professor_by_id(professor_id)
    
    if not professor:
        return "Professor not found"
    
    return render_template("EditProfessor.html", professor=professor)

@admin_bp.route('/update_professor/<professor_id>', methods=['POST'])
def update_professor(professor_id):
    db = get_db()
    admin_id = session.get('userID')
    
    name = request.form.get('name')
    password = request.form.get('password')
    
    if password and password.strip():
        status = adminRepo(db, admin_id).update_professor(professor_id, name, password)
    else:
        status = adminRepo(db, admin_id).update_professor(professor_id, name)
    
    return render_template("EditProfessor.html", 
                          professor={'pID': professor_id, 'pname': name}, 
                          message=status)

@admin_bp.route('/delete_professor/<professor_id>', methods=['POST'])
def delete_professor(professor_id):
    db = get_db()
    admin_id = session.get('userID')
    
    status = adminRepo(db, admin_id).delete_professor(professor_id)
    
    students = adminRepo(db, admin_id).get_all_students()
    professors = adminRepo(db, admin_id).get_all_professors()
    
    return render_template("ManageAccounts.html", 
                          students=students, 
                          professors=professors, 
                          message=status)

@admin_bp.route('/ManageCourses')
def manage_courses():
    db = get_db()
    admin_id = session.get('userID')
    
    courses = adminRepo(db, admin_id).get_all_courses()
    
    return render_template("ManageCourses.html", courses=courses)

@admin_bp.route('/assign_professor/<course_id>')
def assign_professor(course_id):
    db = get_db()
    admin_id = session.get('userID')
    
    course = adminRepo(db, admin_id).get_course_by_id(course_id)
    professors = adminRepo(db, admin_id).get_all_professors()
    
    if not course:
        return "Course not found"
    
    return render_template("AssignProfessor.html", 
                          course=course, 
                          professors=professors)

@admin_bp.route('/update_course_professor/<course_id>', methods=['POST'])
def update_course_professor(course_id):
    db = get_db()
    admin_id = session.get('userID')
    
    professor_id = request.form.get('professor_id')
    
    if not professor_id:
        return "Please select a professor"
    
    status = adminRepo(db, admin_id).assign_professor_to_course(course_id, professor_id)
    
    courses = adminRepo(db, admin_id).get_all_courses()
    
    return render_template("ManageCourses.html", 
                          courses=courses, 
                          message=status)


@admin_bp.route("/AddCourse", methods=["POST"])
def addCourse():
    c_id = request.form["course_id"]
    cname = request.form["course_name"]
    capacity = request.form["capacity"]
    semester = request.form["semester"]
    credits = request.form["credits"]
    professor_id = request.form["professor_id"]

    db = get_db()
    admin_id = session.get('userID')

    status = adminRepo(db, admin_id).add_course(c_id, cname, capacity, semester, credits, professor_id)

    courses = adminRepo(db, admin_id).get_all_courses()

    return render_template("ManageCourses.html", courses=courses, message=status)



@admin_bp.route("/RemoveCourse", methods=["POST"])
def removeCourse():
    c_id = request.form["course_id"]

    db = get_db()
    admin_id = session.get('userID')

    status = adminRepo(db, admin_id).remove_course(c_id)
    courses = adminRepo(db, admin_id).get_all_courses()

    return render_template("ManageCourses.html", courses=courses, message=status)
