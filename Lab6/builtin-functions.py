#Write a Python program with builtin function to multiply all the numbers in a list
'''def mult(list1):
    ans = 1 
    for i in list1: 
        ans *= i
    return ans 
list1 = [1,2,3,4,5]
print(mult(list1))


#Write a Python program with builtin function that accepts a string and 
  #calculate the number of upper case letters and lower case letters

s=input()
upper=0
lower=0
for i in range(len(s)):
    if s[i]>='a' and s[i]<='z':
        lower+=1
    else:
        upper+=1
print(upper, lower) '''


#Write a Python program with builtin function that checks whether a passed string is palindrome or not.

from math import sqrt
from time import sleep
num = int(input())
ms = int(input())
sleep(ms / 1000) #turns sec into msec
sqr = sqrt(num)
print(f"The square root of {num} after {ms} miliseconds is {sqr}.")


#Write a Python program that invoke square root function after specific milliseconds.


def task4(tuple):
    x = all(tuple)
    return x 
tuple1 = (1,2,3,4,5)
print(task4(tuple1))