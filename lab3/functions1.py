#1A recipe you are reading states how many grams you need for the ingredient. 
#Unfortunately, your store only sells items in ounces. 
#Create a function to convert grams to ounces. ounces = 28.3495231 * grams


def grams_to_ounces(x):
	return 28.3495231 * x
 
grams= float(input("enter values in grams: "))
ounces = grams_to_ounces(grams)
print(ounces)

#2Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. The following formula is used for the conversion: C = (5 / 9) * (F – 32)

def f_to_c(f):
    return (5.0/9.0) * (f - 32)

ff=float(input("Enter value in fahrenheit: "))
c = f_to_c(ff)
print("Value in celsius: ", c)


#3Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm.
#How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):
def solve(numheads, numlegs):
    #ns = 'No solutions!'
    for i in range(numheads + 1):
        j = numheads - i
        if 2 * i + 4 * j == numlegs:
            return i, j
    #return ns, ns


if __name__ == "__main__":
    num_heads = 35
    num_legs = 94

    solutions = solve(num_heads, num_legs)
    print(solutions)

#4You are given list of numbers separated by spaces.
    # Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

numbers_list = [2, 5, 10, 13, 15, 17, 33]
prime_numbers = filter_prime(numbers_list)
print("Prime numbers:", prime_numbers)


#5Write a function that accepts string from user and print all permutations of that string.

def toString(List): 
	return ''.join(List) 

def permute(a, l, r): 
	if l == r: 
		print (toString(a)) 
	else: 
		for i in range(l, r + 1): 
			a[l], a[i] = a[i], a[l] 
			permute(a, l + 1, r) 
			a[l], a[i] = a[i], a[l] 

string = "ABC"
n = len(string) 
a = list(string) 
permute(a, 0, n-1) 


#6Write a function that accepts string from user, 
#return a sentence with the words reversed. We are ready -> ready are We

def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = " ".join(reversed(words))
    return reversed_words

sentence = input("Enter a sentence: ")
reversed_sentence = reverse_sentence(sentence)
print("Reversed sentence:", reversed_sentence)




#7Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

# Example 
print(has_33([1, 3, 3]))  # True
print(has_33([1, 3, 1, 3]))  # False
print(has_33([3, 1, 3]))  # False



#8  Write a function that takes in a list of integers and returns True if it contains 007 in order

def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if len(code) == 0:
            return True
    return False

# Example
print(spy_game([1,2,4,0,0,7,5]))  # True
print(spy_game([1,0,2,4,0,5,7]))  # True
print(spy_game([1,7,2,0,4,5,0]))  # False





#9 Write a function that computes the volume of a sphere given its radius
def formula(R):
    return (4/3)*3.141592*R**3

RR = int(input("Enter value for radius: "))
solution=formula(RR)
print("Volume is: ", solution)



# 10Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set.

def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Example 
original_list = [1, 2, 3, 4, 2, 3, 5, 6, 1]
result_list = unique_elements(original_list)
print("Original list:", original_list)
print("List with unique elements:", result_list)



#11Write a Python function that checks whether a word or phrase is palindrome or not. Note: A palindrome is word, phrase,
#or sequence that reads the same backward as forward, e.g., madam

def is_palindrome(word):
    # Remove spaces and convert to lowercase
    word = word.replace(" ", "").lower()
    # Check if the word is equal to its reverse
    return word == word[::-1]

# Example usage
input_word = input("Enter a word or phrase: ")
if is_palindrome(input_word):
    print(f"{input_word} is a palindrome.")
else:
    print(f"{input_word} is not a palindrome.")



#12
    def histogram(numbers):
     for num in numbers:
        print('*' * num)

# Example 
histogram([4, 9, 7])


#13
import random

def guess_the_number():
    name = input("Hello! What is your name? ")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    secret_number = random.randint(1, 20)
    guesses = 0

    while True:
        guess = int(input("Take a guess: "))
        guesses += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break


guess_the_number()
