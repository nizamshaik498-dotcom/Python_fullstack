

class Student:
    institution= 'JBIET'
    student_count=0

    def __init__(self,name,roll_no,gpa):
        self.name=name
        self.roll_no=roll_no
        self.gpa=gpa

    def display(self):
        print(f"[Roll no:{self.roll_no},Name:{self.name},GPA{self.gpa}]")

    def is_distinction(self):
        return self.gpa >=9.0

    def __str__(self):
        return f'Student({self.name},{self.roll_no})'

s1= Student('charan','AI23001',8.75)
s2=Student('Alice','AI23002',9.2)
s1.display()
print(s2.is_distinction())
print("Total students: ",Student.student_count)
print(s1)