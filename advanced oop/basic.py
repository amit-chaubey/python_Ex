###Q1

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_info(self):
        return f'Name: {self.name}, Age:{self.age}, Grade: {self.grade}'

###Q2

class Classroom:
    def __init__(self, class_name, students):
        self.class_name = class_name
        self.students = students

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)

    def list_students(self):
        print(f"Student in {self.class_name}:")
        for student in self.students:
            print(student.get_info())

s1 = Student("Amit", 20, 90)
s2 = Student("Raj", 21, 85)
s3 = Student("Raj", 21, 85)

classroom = Classroom("Class 10", [])

classroom.add_student(s1)
classroom.add_student(s2)
classroom.add_student(s3)

classroom.list_students()