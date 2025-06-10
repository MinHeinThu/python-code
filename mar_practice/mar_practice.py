# OOP practice


class Vector:
    def __init__(self, x , y): # Constructor
        self.x = x
        self.y = y
    

    # Overide + to add vectors

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    def __str__(self):
        return f'Vector {self.x}, {self.y}'

v1 = Vector(2, 3)
v2 = Vector(3, 5)
v3 = v1 + v2

print(v3)