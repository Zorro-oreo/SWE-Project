from flask_login import UserMixin

class Student(UserMixin):
    def __init__(self, sID: str, sname: str, password: str):
        self.sID = sID
        self.sname = sname
        self.password = password

    def get_id(self):
        return f"student_{self.sID}"
    
    def get_GPA(self, grades):
        total_points = 0
        total_credits = 0

        grade_points = {
            'A+': 4.0,
            'A': 4.0,
            'A-': 3.7,
            'B+': 3.3,
            'B': 3.0,
            'B-': 2.7,
            'C+': 2.3,
            'C': 2.0,
            'C-': 1.7,
            'D+': 1.3,
            'D': 1.0,
            'F': 0.0
        }
        for record in grades:
            grade = record['grade']
            if grade in grade_points:
                points = grade_points[grade]
                credits = record.get('credits', 0)
                
                total_points += points * credits
                total_credits += credits

        if total_credits == 0:
            return 0.0

        gpa = total_points / total_credits
        return round(gpa, 3)
