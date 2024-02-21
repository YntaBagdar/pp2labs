#Create a generator that generates the squares of numbers up to some number N.

def gensquares(N):
    for i in range(N):
        yield i**2

g = gensquares(10)
print(next(g))



#Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.


def EvenGenerator(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1


n = int(input())
values = []
for i in EvenGenerator(n):
    values.append(str(i))

print (",".join(values))


#Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.



n = int(input())
divisGenerator = (i for i in range(n))
for i in divisGenerator:
    if (i % 3 == 0) and (i % 4 == 0):
        print(i)


#Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.


a,b = int(input()), int(input())
squaresGenerator = (i * i for i in range(a, b))
for i in squaresGenerator:
    print(i)


#Implement a generator that returns all numbers from (n) down to 0.def gensquares(N):


n = int(input())
listGenerator = (i for i in range(n, 0, -1))
for i in listGenerator:
    print(i)