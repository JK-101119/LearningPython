# Basic function for adding two values.
# def myFun():
#     a = 5
#     b = 6
#     c = a + b
#     print(c)
#
#
# myFun()
#
#
# Function with parameter and arguments.
#
# def myFun(a, b):  # Here a and b are parameters.
#     c = a + b
#     print(c)
#
#
# myFun(5, 6)  # Here 5 and 6 are arguments.


# Function with default parameter.

# Here xyz@gmial.com is a default parameter for those function call that have single argument passed.
# def myFunction(name, email="xyz@gmail.com"):
#     print(name)
#     print(email)


# myFunction('alex', 'alex@gmail.com')
# myFunction('raven')  # Here xyz@gmail.com will automatically called as default argument.
# myFunction('danny', 'danny@gmail.com')
#

# Single parameter with multiple arguments.(*args)

# def argFun(name, *address):
#     print(name)
#     for i in address:
#         print(i)


# Here all addresses will be stored in a single parameter that is address. We can retrieve it with for loop.
# argFun('Danny', 'California', 'Egypt', 'Madagascar')


# Single parameter with multiple keyword arguments.(**kwargs)
# def kwargFun(name, **address):
#     print(name)
#     for i, j in address.items():
#         print(i, ':', j)


# Here all addresses will be stored in a single parameter that is address. We can retrieve it with for loop.
# kwargFun('Danny', home='California', holidays='Egypt', workplace='Madagascar')

# global and globals() variables declarations.
# a = 15  # Here a is global variable.


# def globalFun():
# b = 1   # Here a is local variable.
# global b  # But here we define a as global variable for accessing outside of the function.
# print(' local :', a)
# x = globals()['a']  # Here we call all global variables with globals() function and select a from them.
# globals()['a'] = 10


# globalFun()
# print('global :', a)
# print(id(a))
# print(id(a))

# Passing list to a function and check whether a given number is even or odd.

# def count(lst):
#     even = 0
#     odd = 0
#     for i in lst:
#         if i % 2 == 0:
#             even += 1
#         else:
#             odd += 1
#     return even, odd
#
#
# num = int(input("Enter the number of values you want to check : "))
# lst = []
# for i in range(num):
#     val = int(input("Enter new values to check : "))
#     lst.append(val)
#
# even, odd = count(lst)
# # print("Even : {} and Odd : {}".format(even, odd))
# print(f"Even : {even} and Odd : {odd}")

# Getting string by user input and check whether the length of string is greater than 5.

# Lambda functions or Anonymous Functions.

# add = lambda a, b: a + b
# result = add(5, 6)
# print(result)

# Use of lambda function with filter(), map() and reduce() functions.
from functools import reduce

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(filter(lambda n: n % 2 == 0, lst))
odd = list(filter(lambda n: n % 2 != 0, lst))
double = list(map(lambda n: n * 2, odd))
sumAll = reduce(lambda a, b: a + b, lst)
print(even)
print(odd)
print(double)
print("Sum of all values :", sumAll)
