###Question 1
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, {self.name}! You are {self.age} years old.")

person1  = Person("Rajesh", 20)

print(person1.name)
print(person1.age)

###Question 2
class Student(Person):
    count = 0
    def __init__(self,name,age,roll_no, grade):
        super().__init__(name,age)
        self.roll_no = roll_no
        self.grade = grade
        Student.count += 1

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

student1 = Student("Rajesh", 20, 123, "A")
student1.show_info()

###Question 3 - override greet method in Student class
class Student(Person):
    def __init__(self, name, age, roll_no, grade):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.grade = grade

    def greet(self):
        print(f"Hello, {self.name}! You are {self.age} years old. Your roll number is {self.roll_no} and your grade is {self.grade}.")

student1 = Student("Rajesh", 20, 123, "A")
student1.greet()

###Question 4 - add a class method to Student class to count the number of students
class Student(Person):
    count = 0
    def __init__(self, name, age, roll_no, grade):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.grade = grade
        Student.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

student1 = Student("Rajesh", 20, 123, "A")
student2 = Student("Rajesh", 20, 123, "A")
print(Student.get_count())

