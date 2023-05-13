n = int(input("Please enter a Integer input for which you want to calculate factorial: "))
old_n = n
prod = 1
while n > 1:
    prod *= n
    n -= 1

print(f"The value of {old_n} factorial is {prod}")


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(old_n))