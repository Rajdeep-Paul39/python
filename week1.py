#1
print("Hello, World!")

#2
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_result = num1 + num2

print(f"The sum of {num1} and {num2} is {sum_result}")
#3
num = int(input("Enter a number: "))
square = num * num
print(f"The square of {num} is {square}")
#4
name = input("Enter your name: ")
print(f"Hello, {name}! Welcome!")
#5
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")
#6
def unique_elements(lst):
    return list(set(lst))


numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_numbers = unique_elements(numbers)
print("Unique elements:", unique_numbers)
#7
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)

print(f"{celsius}°C is equal to {fahrenheit}°F")
#8
import math 

def circle_area(radius):
    return math.pi * (radius ** 2)

radius = float(input("Enter the radius of the circle: "))
area = circle_area(radius)

print(f"The area of the circle with radius {radius} is {area:.2f}")
#9
def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

text = input("Enter a string: ")
print(f"Reversed string: {reverse_string(text)}")
#10
import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

number = int(input("Enter a number: "))

if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
  #11
def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

number = int(input("Enter a number: "))
print(f"The factorial of {number} is {factorial(number)}")
#12
def find_largest(lst):
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest

numbers = [1, 3, 7, 2, 9, 4]
largest = find_largest(numbers)
print(f"The largest number in the list is: {largest}")
#13
def check_number_in_range(num, start, end):
    if start <= num <= end:
        return True
    else:
        return False

# Taking user input
number = int(input("Enter a number: "))
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

if check_number_in_range(number, start_range, end_range):
    print(f"{number} is within the range {start_range} to {end_range}.")
else:
    print(f"{number} is not within the range {start_range} to {end_range}.")
#14
def count_case_letters(s):
    upper_case = 0
    lower_case = 0

    for char in s:
        if char.isupper():
            upper_case += 1
        elif char.islower():
            lower_case += 1
    
    return upper_case, lower_case

text = input("Enter a string: ")

upper, lower = count_case_letters(text)
print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")






