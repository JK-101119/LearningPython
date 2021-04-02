# Creating and defininf variable-
# In Python a variable is created when it assigned a value to it. like -

#x = 5

# Here we created a variable x and stored a value 5 to it.
# In Python we don't need to define any data type to a variable untill needed. But for some reasion if we have to define it's type we can simply do it by this -

'''x = "5"
print(x)
x = int(5)
print(x)
x = float(5)
print(x)
print("\n") '''  # Here we use "\n" for printing result in new line.

# We can simply know the type of a variable by type() method.

'''x = "5"
print(type(x))
x = int(5)
print(type(x))
x = float(5)
print(type(x))'''

# Variable names - It can starts with letters or underscore symbol. It cann't be started with numbers but can be ended. Variables name are case-sensitive means A and a are differengt form eachothers.

# Python allows us to assign values to multiple variables in one line -

'''x, y, z = 1, 2, 3
print(x)
print(y)
print(z)
print("\n")'''

# We can assign the same value to multiple variables in one line -

'''x = y = z = "Apple"
print(x)
print(y)
print(z)'''

# If you have a collection of values in a list, tuple etc. Python allows you extract the values into variables. This is called unpacking.

'''nums = [1, 2, 3]
x, y, z = nums
print(x)
print(y)
print(z)'''

# To combine both text and a variable, Python uses the + character.

'''x = "Jitendra Paswan"
print("My name is : " + x )'''

# Normally, when we create a variable inside a function, that variable is local, and can only be used inside that function. But we can create a global variable inside a function, by using global keyword.

'''def myFunction():
    x = "localVar"
    global y
    y = "globalar"
    print(x)
myFunction()
print(y)'''