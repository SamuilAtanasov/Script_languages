import math

class Triangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def hypotenuse(self):
        return math.sqrt(self.a**2 + self.b**2)
    def area(self):
        return (self.a * self.b) / 2
    def perimeter(self):
        return self.a + self.b + self.hypotenuse()
    
t = Triangle(6, 8)

print("Hypotenuse:", t.hypotenuse())
print("Area:", t.area())
print("Perimeter:", t.perimeter())