DELETE FROM Registered_In;
DELETE FROM Course;
DELETE FROM Professor;
DELETE FROM Student;
DELETE FROM Admin;

INSERT INTO Admin (aID, aname, pass) VALUES ('A01', 'System Admin', 'admin123');

INSERT INTO Student (stID, sname, pass) VALUES 
('S01', 'Alice Smith', 'pass123'),
('S02', 'Bob Jones', 'pass123'),
('S03', 'Charlie Day', 'pass123'),
('S04', 'Diana Prince', 'pass123');

INSERT INTO Professor (pID, pname, pass) VALUES 
('P01', 'Dr. Alan Turing', 'prof123'),
('P02', 'Dr. Grace Hopper', 'prof123');

INSERT INTO Course (cID, cname, capacity, PrID) VALUES 
('CS101', 'Intro to Python', 30, 'P01'),
('CS102', 'Data Structures', 25, 'P01'),
('MATH101', 'Calculus I', 50, 'P02');

INSERT INTO Registered_In (stuID, coID, grade) VALUES 
('S01', 'CS101', 'A'),
('S01', 'MATH101', NULL),
('S02', 'CS101', 'B+'),
('S03', 'CS102', 'A-'),
('S04', 'MATH101', NULL);