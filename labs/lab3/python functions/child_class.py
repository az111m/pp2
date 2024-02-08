import math

class MyShape:
    def __init__(self, color="black", is_filled=True):
        self.color = color
        self.is_filled = is_filled

    def __str__(self):
        return f"Color: {self.color}, Filled: {self.is_filled}"

    def getArea(self):
        return 0

class Rectangle(MyShape):
    def __init__(self, color="black", is_filled=True, x_top_left=0, y_top_left=0, length=1, width=1):
        super().__init__(color, is_filled)
        self.x_top_left = x_top_left
        self.y_top_left = y_top_left
        self.length = length
        self.width = width

    def getArea(self):
        return self.length * self.width

    def __str__(self):
        return f"Color: {self.color}, Filled: {self.is_filled}, X Top Left: {self.x_top_left}, Y Top Left: {self.y_top_left}, Length: {self.length}, Width: {self.width}"

class Circle(MyShape):
    def __init__(self, color="black", is_filled=True, x_center=0, y_center=0, radius=1):
        super().__init__(color, is_filled)
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius

    def getArea(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Color: {self.color}, Filled: {self.is_filled}, X Center: {self.x_center}, Y Center: {self.y_center}, Radius: {self.radius}"

rectangle = Rectangle("red", True, 2, 3, 5, 10)
circle = Circle("blue", False, 0, 0, 3)

print("Rectangle properties:", rectangle)
print("Rectangle area:", rectangle.getArea())

print("Circle properties:", circle)
print("Circle area:", circle.getArea())