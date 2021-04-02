# Swapping of two values.
# a = 5
# b = 7
# print("a :", a, "b :", b)
# temp = a
# a = b
# b = temp
# print("a :", a, "b :", b)


def sort(num):
    for i in range(len(num)-1, 0, -1):
        for j in range(i):

            # Swapping of two values.
            if num[j] > num[j+1]:
                temp = num[j]
                num[j] = num[j+1]
                num[j+1] = temp


n = [5, 10, 3, 8, 6, 2, 7, 13, 9, 15, 1]
print("Unsorted List:", n)
sort(n)
print("  Sorted List:", n)
