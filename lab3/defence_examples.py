#Functions
# 1. Calculate factorial using recursion
def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

# 2. Reverse a string
def reverse_string(string):
    return string[::-1]

# 3. Get the maximum of three numbers
def get_max(a, b, c):
    return max(a, b, c)

# 4. Check if a number is even
def is_even(num):
    return num % 2 == 0

# 5. Filter prime numbers from a list
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

# 6. Find common elements between two lists
def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

# 7. Word frequency in a string
def word_frequency(string):
    words = string.split()
    freq_dict = {}
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1
    return freq_dict

# 8. Fibonacci using recursion
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# 9. Calculate running average
def calculate_running_average(numbers):
    running_sum = 0
    averages = []
    for i, num in enumerate(numbers, start=1):
        running_sum += num
        averages.append(running_sum / i)
    return averages



#Classes and Objects

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

    