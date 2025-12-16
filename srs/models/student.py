class Student:
    def __init__(self, sID: str, sname: str, password: str):
        self.sID = sID
        self.sname = sname
        self.password = password      

    def calcGPA(self, courseGrades): #Assuming all courses are 3 credit

        totalHours = 0
        totalQpoints = 0

        for grade in courseGrades:

            totalHours += 3

            if (grade == 'A'):

                totalQpoints += 4 * 3

            elif (grade == 'A-'):
                
                totalQpoints += 3.7 * 3

            elif (grade == 'B+'):
                
                totalQpoints += 3.3 * 3

            elif (grade == 'B'):
                
                totalQpoints += 3.0 * 3

            elif (grade == 'B-'):
                
                totalQpoints += 2.7 * 3

            elif (grade == 'C+'):
                
                totalQpoints += 2.3 * 3

            elif (grade == 'C'):
                
                totalQpoints += 2.0 * 3

            elif (grade == 'D+'):
                
                totalQpoints += 1.3 * 3

            elif (grade == 'D'):
                
                totalQpoints += 1 * 3

            elif (grade == 'F'):
                
                totalQpoints += 0

            return totalQpoints / totalHours