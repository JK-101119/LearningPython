#There are three numeric types in Python -

# int - Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length

x = 5
print(type(x))

# float - Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

x = 5.5
print(type(x))

# complex - Complex numbers are written with a "j" as the imaginary part.

x = 5j
print(type(x))

#******************************************************************************************************************

#Swaping of values
a=5
b=6
# By using this method of swapping we are using an extra operator.

# temp=a
# a=b
# b=temp

# By using this method of swapping we aren't using an extra operator but still waisting a bit for that is used for storing 11.

# a=a+b  #5+6
# b=a-b  #11-6
# a=a-b  #11-5

# By using this method of swapping we are using XOR gate.
# a=a^b
# b=a^b
# a=a^b
#But Python provides a best way to swap a value that is -
a,b = b,a

print("a =",a)
print("b =",b)