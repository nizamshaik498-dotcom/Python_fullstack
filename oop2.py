
class Person:
    def __init__(self,name,age);
        self.name=name
        self.age=age

    def greet(self):
        print(f'hi , iam {self.name}, {self.age} years old')

class Student(Person):
    def __init__(self,name,age,roll_no):
        super().__init__(name,age)
        self.roll_no=roll_no

    def study(self):
        print(f'{self.name} is studying')

s=Student('Charan',28,'AI23001')
s.greet()
s.study()
print(isinstance(s, Person))
