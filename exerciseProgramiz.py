# Python Program to Print Hello world!
# print("Hello World")

# Python Program to Add Two Numbers
# a = int(input("Enter first number : "))
# b = int(input("Enter second number : "))
# c = a + b
# print("Sum :", c)

# Python Program to Find the Square Root
# x = int(input("Enter a number to find square : "))
# square = x ** 0.5
# print(square)

# Python Program to Calculate the Area of a Triangle
# base = int(input("Enter base : "))
# height = int(input("Enter height : "))
# area = (height * base) / 2
# print("Are of Triangle : ", area)

# Python Program to Solve Quadratic Equation
# a = int(input("Enter value of ax^2 : "))
# b = int(input("Enter value of bx : "))
# c = int(input("Enter value of c : "))
# alpha = (-b + (b ** 2 - 4 * a * c) ** 0.5) / 2 * a
# beeta = (-b - (b ** 2 - 4 * a * c) ** 0.5) / 2 * a
# print(f"X : {alpha} Y : {beeta}")

# Python Program to Swap Two Variables
# a = 5
# b = 7
# print(f"a : {a} b : {b}")
# temp = a
# a = b
# b = temp
# print(f"a : {a} b : {b}")

# Python Program to Generate a Random Number
# import random
#
# x = random.randint(1, 11)
# print("Random :", x)

# Python Program to Convert Kilometers to Miles
# km = float(input("Enter a KM value to convert into Miles :"))
# miles = km * 0.625
# print(f"{km} is equal to", miles)

# Python Program to Convert Celsius To Fahrenheit
# cel = float(input("Enter a value in Celsius : "))
# far = (1.8 * cel) + 32
# print(f"{cel} is equal to {far}")

# Python Program to Check if a Number is Positive, Negative or 0
# num = float(input("Enter a number:"))
# if num > 0:
#     print("positive number")
# elif num == 0:
#     print("Zero")
# else:
#     print("Negative")

# Python Program to Check if a Number is Odd or Even
# x = int(input("Enter a number to check : "))
# if x % 2 == 0:
#     print(f"{x} is Even")
# else:
#     print(f"{x} is Odd")

# Python Program to Check Leap Year
# year = int(input("Enter a year to check : "))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")

# Python Program to Find the Largest Among Three Numbers
# num1 = float(input("Enter first number : "))
# num2 = float(input("Enter second number : "))
# num3 = float(input("Enter third number : "))
# if num1 > num2 and num1 > num3:
#     great = num1
#     print(f"{great} is Largest")
# elif num2 > num1 and num2 > num3:
#     great = num2
#     print(f"{great} is Largest")
# else:
#     great = num3
#     print(f"{great} is Largest")

# Python Program to Check Prime Number
# counter = False
# num = int(input("Enter a number to check : "))
# if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             counter = True
#             break
# if counter:
#     print(f"{num} is a Prime Number")
# else:
#     print(f"{num} is not a Prime Number")

# Python Program to Print a ll Prime Numbers in an Interval
# start = int(input("Enter start : "))
# end = int(input("Enter end : "))
# for num in range(start, end + 1):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)

# Python Program to Find the Factorial of a Number
# By using for loop only.
# fact = 1
# num = int(input("Enter a number to find factorial : "))
# for i in range(1, num + 1):
#     fact = fact * i
# print("The factorial of", num, "is", fact)

# By using function.
# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n-1)
#
#
# num = int(input("Enter a number to find factorial : "))
# if num < 0:
#     print("Invalid input")
# elif num == 0:
#     print("Factorial is 1")
# else:
#     print(f"Factorial of {num} is", fact(num))

# Python Program to Display the multiplication Table
# num = int(input("Enter a number to print table : "))
# for i in range(1, 11):
#     tab = num * i
#     print(num, "*", i, " = ", tab)

print('---------------------------------------------')
# Python Program to Print the Fibonacci sequence
# Python Program to Check Armstrong Number
# Python Program to Find Armstrong Number in an Interval

# Python Program To Display Powers of 2 Using Anonymous Function
# term = int(input("Enter number of terms : "))
# for i in range(term):
#     y = lambda n: 2 ** i
#     print("2 *", i, "=", y(term))

# a = 5
# b = 7
# d = 8
# c = lambda n: a + b + d
# print("Sum : ", c([a, b, d]))
# print("Sum : ", c([]))
