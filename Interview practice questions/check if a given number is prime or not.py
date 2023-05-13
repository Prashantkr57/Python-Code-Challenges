def is_prime(n):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input("Enter a number you want to check if it is prime or not: "))
print(is_prime(num))
