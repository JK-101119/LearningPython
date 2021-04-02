# a = -1
#
#
# def search(ls, c):
#     i = 0
#     while i < len(lst):
#         if lst[i] == n:
#             globals()['a'] = i
#             return True
#         i = i + 1
#     else:
#         return False


a = -1


def search(li, c):
    for i in range(len(lst)):
        if lst[i] == n:
            globals()['a'] = i
            return True
    else:
        return False


lst = [1, 3, 5, 7, 9]
n = 5
if search(lst, n):
    print("Found at", a + 1, "position")
else:
    print("Not Found!")
