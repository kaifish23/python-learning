#Problem 1: Shape Calculator with Polymorphism
#Part A: Abstract Shape Class
from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    def describe(self):
        return f"this is a {self.__class__.__name__}"
    @staticmethod
    def validate_positive(value, name):
        if value > 0:
            return True
        else:
            print(f"{name} must be positive!")
            return False
        
#Part B: Concrete Shape Classes
class Circle(Shape):
    def __init__(self, radius):
        if Shape.validate_positive(radius, "Radius"):
            self.radius = radius
        else:
            self.radius = 0
    def area (self):
        return 3.14159 * (self.radius ** 2)
    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        if Shape.validate_positive(width, "Width") and Shape.validate_positive(height, "Height"):
            self.width = width
            self.height = height 
        else:
            self.width = 0
            self.height = 0
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
    
class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        if (Shape.validate_positive(side1, "Side1") and
            Shape.validate_positive(side2, "Side2") and
            Shape.validate_positive(side3, "Side3")):
            self.side1 = side1
            self.side2 = side2
            self.side3 = side3
        else:
            self.side1 = self.side2 = self.side3 = 0
    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

#Part C: ShapeCollection Class
class ShapeCollection:
    def __init__(self):
        self.shapes = []
    def add_shape(self, shape):
        self.shapes.append(shape)
    def total_area(self):
        return sum(shape.area() for shape in self.shapes)
    def total_perimeter(self):
        return sum(shape.perimeter() for shape in self.shapes)
    
#test code
if __name__ == "__main__":
    #create shapes
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(3, 4, 5)
    #test individual shapes
    print("Individual Shapes:")
    for shape in [circle, rectangle, triangle]:
        print(f"{shape.describe()}")
        print(f"Area: {shape.area():.2f}")
        print(f"Perimeter: {shape.perimeter():.2f}")
    #test collection (polymorphism)
    collection = ShapeCollection()
    collection.add_shape(circle)
    collection.add_shape(rectangle)
    collection.add_shape(triangle)
    print(f"\nCollection Totals:")
    print(f" Total Area: {collection.total_area():.2f}")
    print(f" Total Perimeter: {collection.total_perimeter():.2f}")
    #test validation
    print("\nTesting validation:")
    try:
        bad_circle = Circle(-5)
    except:
        print("Correctly rejected negative radius")
print("="*50)

