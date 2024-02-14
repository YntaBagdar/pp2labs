#Create class My_shape with params color(String) and is_filled (boolean) 
#create __init__() method with default values for color and is_filled
#(choose your own default values) override __str__() method (choose your own 
#logic of string generating which includes inner fields values) create method 
#getArea() which returns 0;
class My_shape:
    def __init__(self, color="black", is_filled=False):
        self.color = color
        self.is_filled = is_filled

    def __str__(self):
        return f"Color: {self.color}, Filled: {self.is_filled}"
    
    def getArea(self):
        return 0
class Rectangle(My_shape):
    def __init__(self, color="black", is_filled=False,
                       x_top_left=0, y_top_left=0, length=1, width=1):
        super()._init_(color, is_filled)
        self.x_top_left = x_top_left
        self.y_top_left = y_top_left
        self.length = length
        self.width = width

def getArea(self):
        return self.length * self.width

    def _str_(self):
        return f"Rectangle: {super()._str_()}, 
             Top Left: ({self.x_top_left}, {self.y_top_left}), 
             Length: {self.length}, Width: {self.width}"

  
      




"""
Create child classes Rectangle and Circle which extend My_shape class add extra 
fields for Rectangle (x_top_left, y_top_left, length, width) add extra fields 
for Circle (x_center, y_center, radius) in each if Rectangle and Circle override
 method getArea() based on length and width of Rectangle, and radius of Circle 
 override __str__() method (add extra fields to reslting string)

Create a console input for Rectangle creation, and output it with all its fields
 included in the output."""


#inher
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()