# Array is the collection of same data types of elements but we have to define its data type first.
from array import *

oldArr = array('i', [10, 15, 20, 35])

# print(oldArr.typecode, end="")
# print("\n")
# print(oldArr.itemsize, end="")
# print("\n")
#
# oldArr.append(18)
# print(oldArr, end="")
# print("\n")
#
# print(oldArr.buffer_info(), end="")
# print("\n")
# print(oldArr.byteswap(), end="")

# print(oldArr.buffer_info(), end="")
# print("\n")
# print(oldArr.count(10), end="")

# print("\n")
# print(oldArr.index(35), end="")
# print("\n")
# print(oldArr.insert(0, 13), end="")
# print("\n")
# print(oldArr.pop(1))
# print("\n")
# print(oldArr.remove(10))
# print("\n")
# print(oldArr.reverse())
# print("\n")
# print(oldArr)
# print(oldArr.tobytes())
# print(oldArr.tolist())

# Print array elements one by one by for loop.

# for i in oldArr:
#     print(i)

# Copy an array to a new array form previous one.

# newArr = array(oldArr.typecode, (a for a in oldArr))
# for e in newArr:
#     print(e)

# Creating array by getting elements form user.

# arr = array('i', [])
# lenArr = int(input("Enter the length of array  : "))
# for i in range(lenArr):
#     e = int(input("Enter next element : "))
#     arr.append(e)
# print(arr)

# Searching array element in array by loop.

# getArr = int(input("Enter the array element to search : "))

# for j in arr:
#     if arr.count(j) == getArr:
#         break
# print("Found on index", getArr.__index__())

# Searching array element in array by function.

# print("Found on index", (arr.index(getArr)))

