from unittest.mock import MagicMock, patch

@patch("srs.controllers.student_controller.current_user")
@patch("srs.controllers.student_controller.studentRepo")
def test_student_view_grades(mock_repo_class, mock_current_user, client):
   
    mock_instance = MagicMock()
    mock_repo_class.return_value = mock_instance
  
    mock_instance.get_grades.return_value = [
        {'course': 'CSAI203', 'grade': 'A', 'credits': 3},
        {'course': 'MATH101', 'grade': 'B', 'credits': 3}
    ]

    mock_current_user.sID = "S01"
    mock_current_user.is_authenticated = True
    mock_current_user.get_GPA.return_value = 3.5
 
    response = client.get("/view_grades")

    
    assert response.status_code == 200

@patch("srs.controllers.student_controller.current_user")
@patch("srs.controllers.student_controller.studentRepo")
def test_student_register_course_success(mock_repo_class, mock_current_user, client):

    mock_instance = MagicMock()
    mock_repo_class.return_value = mock_instance

    mock_instance.RegisterCourse.return_value = None 

    mock_current_user.sID = "S01"
    mock_current_user.is_authenticated = True

    response = client.post("/register_course", data={
        "course_id": "CSAI203"
    })

    assert response.status_code == 200