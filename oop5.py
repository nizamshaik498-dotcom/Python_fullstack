

class Vector:
    def __init__(self, x, y):
        self.x ,self.y = x, y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, k):
        return Vector(self.x * k, self.y * k)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __len__(self):
        return int((self.x ** 2 + self.y ** 2) ** 0.5)

v1 = Vector(3, 4)
v2 = Vector(1, 2)
print(v1)          # Vector(1, 2)
print(v1+v2)
print(v1*2)
print(len(v1))
print(v1==Vector(3, 4))  # True