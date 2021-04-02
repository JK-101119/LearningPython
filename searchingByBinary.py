a = -1


def search(ls, c):
    lower = 0
    upper = len(lst) - 1

    while lower <= upper:
        mid = (lower + upper) // 2
        if lst[mid] == n:
            globals()['a'] = mid
            return True
        else:
            if lst[mid] < n:
                lower = mid + 1
            else:
                upper = mid - 1
    else:
        return False


lst = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
n = 29
if search(lst, n):
    print("Found at", a + 1, "position")
else:
    print("Not Found!")
