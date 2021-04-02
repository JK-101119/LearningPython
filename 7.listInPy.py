# List is a collection of changeable, iterable, ordered and different data types items.

nums = [1, 8, 10, 2, 7, 9, 5, 4, 6, 3]
lst = ["java", "python", "javascript", "html"]
mixed = [1, 2, "Apple", False, True, "Orange"]
myTuple = ("Danny", "Jen")

# List Constructor method to create a list.

# cons = list(("Pen", "Pencil", "Mouse", "Keyboard"))
# print(cons)

# Creates a list using range of 10 by comprehension method.

# myList = [x for x in range(10)]
# print(myList)

# Printing/Accessing items of a list.

# print(lst)
# print(lst[0])
# print(lst[1:])
# print(lst[:2])
# print(lst[1:3])
# print(lst[-1:])
# print(lst[:-2])
# print(lst[-3:-1])

# Iteration of list elements.
# for i in lst:
#     print(i)

# i = 0
# while i <= len(nums):
#     print(i)
#     i += 1

# [print(x) for x in nums]

# Iterating index of elements.
# for i in range(len(lst)):
#     print(i)

# Adding list items.

# lst[0] = "CPP"
# print(lst)
# lst[-1] = "Django"
# print(lst)
# lst[-1:-3] = "Flask", "MongoDB"
# print(lst)
# lst[1:3] = "PHP", "Linux"
# print(lst)
# lst[1:2] = "PHP", "Linux", "ML"
# print(lst)

# Searching in list.

# if 'java' in lst:
#     print('Yes ! Found.')

# creating a new list form existing list elements.

# newList = []
# for x in nums:
#     if x % 2 != 0:
#         newList.append(x)
# print(newList)

# ------------------------------------------ or --------------------------------------
# Note - list of numbers is not iterable by this comprehension method.
# lstNew = [x for x in lst if 'a' in x]
# print(lstNew)


# Concatenating multiple list items.

# lst2 = ["Python", "MySql"]
# lst = lst + lst2
# print(lst)

# for x in lst2:
#     lst.append(x)
# print(lst)

# lst.extend(lst2)
# print(lst)

# lst.extend(myTuple)
# print(lst)

# List methods -

# print(type(lst))

# lst.append("XML")
# print(lst)
#
# lst.remove("html")
# print(lst)

# lst.pop(1)
# print(lst)
#
# lst.pop()
# print(lst)

# lst.insert(0, "Ruby")
# print(lst)

# c = lst.count('html')
# print(c)

# i = lst.index('python')
# print(i)

# Shorting list items by using own created function.

# nums.sort()
# print(nums)

# print(len(nums))

# nums.reverse()
# print(nums)

# lst.clear()
# print(lst)

# del lst
# print(lst)
