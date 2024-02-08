#Write a function that computes the volume of a sphere given its radius
def formula(R):
    return (4/3)*3.141592*R**3

RR = int(input("Enter value for radius: "))
solution=formula(RR)
print("Volume is: ", solution)
