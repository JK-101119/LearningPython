# Program to check whether a number is palindrome or not.
# Getting string input by user.

s = input("Enter a string to check : ")

# Extracting start and end character of the string.

start = 0
end = len(s) - 1

# Checking the conditions.
while start < end:
    if s[start] == s[end]:
        start = start + 1
        end = end - 1
    else:
        break

# Checking and Printing result.
if start < end:
    print("Palindrome Not")
else:
    print("Palindrome")
