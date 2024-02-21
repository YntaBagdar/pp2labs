#1. Write a Python program to convert degree to radian.
#Input degree: 15
#Output radian: 0.261904

def degreeToRadian(D):
    return D * 0.01746027 
degree = 15
radian = degreeToRadian(degree)
print("radian:", radian )



#2. Write a Python program to calculate the area of a trapezoid.
#Height: 5
#Base, first value: 5
#Base, second value: 6
#Expected Output: 27.5

# Area = ½ x (Sum of parallel sides) x (perpendicular distance between the parallel sides).
# Area = ½ h (b 1 + b 2).

def areaOfTrapezoid(Height, Base1, Base2):
    return (Height* (Base1+Base2))/2
Height = 5
Base1 = 5
Base2 = 6
area = areaOfTrapezoid(Height, Base1, Base2)
print( area)




#3. Write a Python program to calculate the area of regular polygon.
#Input number of sides: 4
#Input the length of a side: 25
#The area of the polygon is: 625
# ½ (a × p)

def areaOfRegPolygon(numofsides, lengthofsides):
    return (numofsides * lengthofsides * (lengthofsides* 0.5))/2
numofsides = 4
lengthofsides = 25
area = areaOfRegPolygon(numofsides, lengthofsides)
print( "The area of the polygon is:", area)


#4. Write a Python program to calculate the area of a parallelogram.
#Length of base: 5
#Height of parallelogram: 6
#Expected Output: 30.0
# A = (b * h) 

def areaOfParallelogram(length, height):
    return length*height
length= 5
height= 6
area = areaOfParallelogram(length, height)
print("A =", area )