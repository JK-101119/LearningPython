# There are following types of data - 

#string type - It can be a single character or a word or a sentance.
x = "Hello World"
print(type(x))

#Integr(int) - It is whole numbers that can be negative or positive, but without decimal.
x = 20
print(type(x))

#Floating Point(float) -  It is whole numbers that can be negative or positive, but with decimal value.
x = 20.5
print(type(x))

#Complex(j) - It is whole numbers that can be negative or positive, but there is an imaginary number associated with it.
x = 1j
print(type(x))

#List[] - It is collection of items saperated by commas that can be of different data types.
x = ["apple", "banana", "cherry"]	
print(type(x))

#Tuples() - Tuples are used to store multiple items in a single variable.
x = ("apple", "banana", "cherry")
print(type(x))

x = range(6)
print(type(x))

#Dictionaries{} - Dictionaries are used to store data values in key:value pairs
x = {"name" : "John", "age" : 36}
print(type(x))

#Set() - A set is a collection values assigned to a single variable which is both unordered and unindexed.
x = {"apple", "banana", "cherry"}
print(type(x))

x = frozenset({"apple", "banana", "cherry"})
print(type(x))

#Booleans - It represent one of two values either True or False.
x = True	
print(type(x))

x = b"Hello"
print(type(x))

x = bytearray(5)	
print(type(x))

x = memoryview(bytes(5))
print(type(x))
