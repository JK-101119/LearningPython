num = eval(input("Enter a number : "))
isPrime = True
for i in range(2, num):
    if num % i == 0:
        isPrime = False
        break
if isPrime:
    print("Prime Number")
else:
    print("Non-prime Number")
