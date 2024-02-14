#Write a function called calculate_factorial that takes 
#a positive integer as a parameter and returns its factorial (use recursion)

def calculate_factorial(k):
    if (k > 0):
        result = k*(k-1)
        print(result)
    else: result=0
    return result
print("\n\nResult is:", calculate_factorial(3))


#Write a function called reverse_string 
#that takes a string as a parameter and returns its reverse.

def reverse_string(string):
 return "".join(reversed(string))
print("the res is:", reverse_string("YNTA") )

#Write a function called get_max that takes three parameters (a, b, and c) 
#and returns the maximum of the three.
def get_max(a, b, c):
   if (a >= b) and (a >= c):
      return a
   elif (b>=a) and (b>=c):
      return b
   else:
      return c
    
print("the max is:", get_max(99, 100, 6))

#Write a function called is_even that takes an integer as a parameter 
#and returns True if it's even and False otherwise.

def is_even(num):
   while num:
       if (num%2==0):
         return True
       elif (num%2!=0):
         return False
print(is_even(222))

#You are given list of numbers separated by spaces. Write a function 
#filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
print("List of integers:")
print(numbers)

prime_numbers = list(filter(is_prime, numbers))
print("\nExtract prime numbers of the said list:")
print(prime_numbers)


#Write a function find_common_elements that takes two lists 
#as parameters and returns a new list containing common elements between them.
a=[1,2,3,5,6]
b=[2,4,5,8,99]
def find_common_elements(a, b):
   c=[value for value in a if value in b]
   return c
result=find_common_elements(a, b)
print(find_common_elements(a, b))

#Write a function word_frequency that takes a string as input 
#and returns a dictionary where keys are unique words,
#and values are their frequencies.

def word_frequency(string):
   

#Write a recursive function fibonacci that returns the nth Fibonacci number.
   

hgu



#Write a function calculate_running_average that takes a series 
#of numbers as input and returns a list containing the running average at each position.
huyg



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

