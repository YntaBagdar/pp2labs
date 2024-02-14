
import math

class MyShape:
    def _init_(self, color="black", is_filled=False):
        self.color = color
        self.is_filled = is_filled
    
    def _str_(self):
        return f"Color: {self.color}, Filled: {self.is_filled}"

    def getArea(self):
        return 0

class Rectangle(MyShape):
    def _init_(self, color="black", is_filled=False, x_top_left=0, y_top_left=0, length=1, width=1):
        super()._init_(color, is_filled)
        self.x_top_left = x_top_left
        self.y_top_left = y_top_left
        self.length = length
        self.width = width
    
    def getArea(self):
        return self.length * self.width

    def _str_(self):
        return f"Rectangle: {super()._str_()}, Top Left: ({self.x_top_left}, {self.y_top_left}), Length: {self.length}, Width: {self.width}"

class Circle(MyShape):
    def _init_(self, color="black", is_filled=False, x_center=0, y_center=0, radius=1):
        super()._init_(color, is_filled)
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius
    
    def getArea(self):
        return math.pi * self.radius ** 2

    def _str_(self):
        return f"Circle: {super()._str_()}, Center: ({self.x_center}, {self.y_center}), Radius: {self.radius}"

# Console input for Rectangle creation
def create_rectangle_from_input():
    color = input("Enter color: ")
    is_filled = input("Is filled? (True/False): ").lower() == "true"
    x_top_left = float(input("Enter x coordinate of top left corner: "))
    y_top_left = float(input("Enter y coordinate of top left corner: "))
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    return Rectangle(color, is_filled, x_top_left, y_top_left, length, width)

# Example usage:
if __name__ == "_main_":
    rectangle = create_rectangle_from_input()
    print(rectangle)
    print("Area:", rectangle.getArea())
