#POLYMORPHISM

import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")
    def describe(self):
        print(f"{type(self).__name__} with area: {self.area():.2f}")

class Circle(Shape):
    def __init__(self,r):self.r=r
    def area(self):
        return math.pi*self.r**2

class Rectangle(Shape):
    def __init__(self,w,h):self.w=w;self.h=h
    def area(self):
        return self.w*self.h

class Triangle(Shape):
    def __init__(self,b,h):self.b=b;self.h=h
    def area(self):
        return 0.5*self.b*self.h

for shape in [Circle(5), Rectangle(4,6), Triangle(3,8)]:
    shape.describe()