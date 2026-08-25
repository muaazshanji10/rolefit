def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

print(celsius_to_fahrenheit(5))

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

print(is_even(4))


def sum_list(numbers):
    total = 0
    for number in numbers:
        total = number + total
    return total

print(sum_list([1,2,3,4]))

def find_max(numbers):
    biggest = numbers[0]      # start by assuming the first item is the biggest
    for number in numbers:
        if number > biggest:
            biggest = number   # found a new biggest — update the tracker
    return biggest             # after checking everything, hand back the answer

print(find_max([1,7,5,3,7,9,0]))


def count_vowels(word):
    total = 0
    for letter in word:
        if letter in "aeiou":
            total = 1 + total
    return total

print(count_vowels("discombobulated"))

def reverse_string(s):
    reversed_S = ""
    for letter in s:
        reversed_S = letter + reversed_S
    return reversed_S

print(reverse_string("dog"))


def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else: 
            print(i)


fizzbuzz(15)

def factorial(n):
    total = 1
    for number in range(1, n+1):
        total = number*total
    return total

print(factorial(5))

def is_palindrome(s):
    if s == reverse_string(s):
        return True
    else:
        return False

print(is_palindrome("racecar"))


def average(numbers):
    return sum_list(numbers)/len(numbers)

print(average([2,4,6,8]))

