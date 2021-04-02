# Tuples are used to store multiple items in a single variable.

myTuple = ('java', 'python', 'linux', 'ruby')

# We can create a tuple with constructor function.

# print(myTuple)
# print(type(myTuple))
# print(len(myTuple))
# print(myTuple.index('linux'))
# print(myTuple.count('java'))

# Creating single item tuple, we must put a comma after item name.

# myTuple = ('a',)
# print(type(myTuple))
# myTuple = ('b')
# print(type(myTuple))

# Accessing tuple items.

# print(myTuple[1])

# Check if a given item exists.
# if 'linux' in myTuple:
#     print("Yes! Got it.")
# else:
#     print("NO! Not found.")

# We cannot change, add or remove tuple's items directly but we can do it with the help of list as done below -
# Thus we can use all the operations on tuples.
# x = list(myTuple)
# x.insert(1, "NewLang")
# myTuple = tuple(x)
# print(myTuple)

# Unpacking a tuple means to extracting the values back into variables.

# fruits = ("apple", "orange", "grapes", "kiwi")
# print(fruits)
# (a, o, g, k) = fruits
# print(a)
# print(o)
# print(g)
# print(k)

# Using asterisk * to store remaining values that are more than variables.

fruits = ("apple", "orange", "grapes", "kiwi", "banana", "guava", "blackberry")
# print(fruits)
# (a, o, g, k, *remain) = fruits
# print(a)
# print(o)
# print(g)
# print(k)
# print(remain)

# If we assign asterisk before the last variable it left the equal values for next and stores remaining value to self.

# (a, o, g, *remain, k) = fruits
# print(a)
# print(o)
# print(g)
# print(k)
# print(remain)

# Loop through tuple values.

# for i in fruits:
#     print(i)

# Loop through tuple indexes.

# for i in range(len(fruits)):
#     print(i)
# To join two or more tuples we can use the + operator.

one = ('one', 'two', 'three')
tow = ('four', 'five', 'six')
one += tow
print(one)
# To multiply the content of a tuple a given number of times, we can use the * operator.

num = (1, 2, 3, 4, 5, 'form here')
num *= 2
print(num)
