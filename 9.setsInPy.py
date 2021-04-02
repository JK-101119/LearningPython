# A set is a collection which is both unordered and unindexed.

mySet = {'apple', 'banana', 'grapes', 'kiwi'}
# print(mySet)

ourSet = set(('apple','google','microsoft'))
# print(mySet)

# Accessing set items.

# for i in mySet:
#     print(i)

# We can get indexes of set but cannot use it for reference.
# for i in range(len(mySet)):
#     print(i)

# It raises an error!
# print(mySet[1])

# We can check for a value.

# if 'grapes' in mySet:
#     print('Yes! Got it.')

# Set methods -

# add() - Add the item in set at random position because in set position is not fixed.
# mySet.add('NewFruit')
# print(mySet)

# clear() - Removes all the item of the set.
# mySet.clear()
# print(mySet)

# copy() - It copies the element of set.
# x = mySet.copy()
# print(x)

# difference() - Returns a set that contains the difference between two sets.
# x = ourSet.difference(mySet)
# print(x)

# symmetric_difference() - It simple merge the elements by leaving duplicate.
# x = mySet.symmetric_difference(ourSet)
# print(x)

# Remove the items that exist in both sets.
mySet.difference_update(ourSet)
print(mySet)