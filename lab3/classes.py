#Define a class which has at least two methods: 
#getString: to get a string from console input.
#printString: to print the string in upper case.

class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()
    
    def printString(self):
        print(self.s.upper())

strObj = InputOutString()
strObj.getString()
strObj.printString()


#Define a class named Shape and its subclass Square. 
#The Square class has an init function which takes a length as argument.
#Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.


class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2
    
#Define a class named Rectangle which inherits from Shape class from task 2.
#Class instance can be constructed by a length and width.
#The Rectangle class has a method which can compute the area.
    class Rectangle(Shape):
     def __init__(self, length, width):
        self.length=length
        self.width=width

        def area(self):
          return self.length * self.width

#Write the definition of a Point class. Objects from this class should have a
#a method show to display the coordinates of the point
#a method move to change these coordinates
#a method dist that computes the distance between 2 points
    
from ast import In
import importlib
import math
from pickletools import pylist
class Point(object):
    """A 2D point in the cartesian plane"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({}, {})'.format(self.x, self.y)

    def dist_to_point(self, Point):
        dist = math.sqrt((self.x - Point.x)**2 + (self.y - Point.y)**2)
        return dist

p1 = Point(4,9)
p2 = Point(10,5)
print(p1.dist_to_point(p2))
# 7.211102550927978


#Create a bank account class that has attributes owner, balance and two methods deposit and withdraw.
#Withdrawals may not exceed the available balance. Instantiate your class, make several deposits and withdrawals,
#and test to make sure the account can't be overdrawn.
#class Account:
    #pass

# Python program to create Bankaccount class
# with both a deposit() and a withdraw() function
class Bank_Account:
	def __init__(self):
		self.balance=0
		print("Hello!!! Welcome to the Deposit & Withdrawal Machine")

	def deposit(self):
		amount=float(input("Enter amount to be Deposited: "))
		self.balance += amount
		print("\n Amount Deposited:",amount)

	def withdraw(self):
		amount = float(input("Enter amount to be Withdrawn: "))
		if self.balance>=amount:
			self.balance-=amount
			print("\n You Withdrew:", amount)
		else:
			print("\n Insufficient balance ")

	def display(self):
		print("\n Net Available Balance=",self.balance)

# Driver code

# creating an object of class
s = Bank_Account()

# Calling functions with that class object
s.deposit()
s.withdraw()
s.display()



#Write a program which can filter prime numbers in a list by using filter function. 
            #Note: Use lambda to define anonymous functions.         
def prime (mylist):
        for i in range(2, 8):
           print (i) # added to make things explicit; it's not necessary
           return filter(lambda x: x == i or x % i, mylist)

def prime2 (mylist):
    nums = mylist
    for i in range(2, 8):
        print (i) # added to make things explicit; it's not necessary
        nums = filter(lambda x: x == i or x % i, nums)
    return nums