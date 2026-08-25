def celsius_to_fahrenheit(celsius):
    farenheit = celsius*9/5 + 32
    return farenheit 

print(celsius_to_fahrenheit(5))

def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False

print(is_even(4))

def sum_list(numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total


def find_max(numbers):
    biggest_n = numbers[0]
    for n in numbers:
        if n>biggest_n:
            biggest_n = n
    return biggest_n

def count_vowels(word):
    total = 0
    for letter in word:
        if letter in "aeiou":
            total = total + 1
    return total
    
def reverse_string(s):
    reversed_s = ""
    for letter in s:
        reversed_s = letter + reversed_s
    return reversed_s

def fizzbuzz(n):
    for n in range(1, n+1):
        if n%3==0 and n%5==0:
            print("FizzBuzz")
        elif n%3==0:
            print("Fizz")
        elif n%5==0:
            print("buzz")
        else:
            print(n)

def factorial_n(n):
    result = 1
    for i in range(1, n+1):
        result = result*i
    return result

print(factorial_n(5))

def is_palindrome(s):
    if reverse_string(s) == s:
        return True
    else:
        return False

print(is_palindrome("racecar"))

def average_n(numbers):
    average = 0
    for n in average(numbers):
    average = sum_list(numbers)/len(numbers)
    return average

print(average_n([1,2,3,4,5,6,7,8,9]))







