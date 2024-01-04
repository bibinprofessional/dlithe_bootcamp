import math

class Geometry:
    def __init__(self, radius=0, length=0):
        self.radius = radius
        self.length =length

    def circle_area(self):
        return math.pi * self.radius**2

    def circle_peri(self):
        return 2 * math.pi * self.radius
       
    def square_area(self):
        return self.length**2
        
    def square_peri(self):
        return 4 * self.length
       


# Circle
c = Geometry(radius=5)
print("Circle Area:", c.circle_area())
print("Circle Perimeter:", c.circle_peri())

# Square 
s = Geometry(length=4)
print("\nSquare Area:", s.square_area())
print("Square Perimeter:", s.square_peri())