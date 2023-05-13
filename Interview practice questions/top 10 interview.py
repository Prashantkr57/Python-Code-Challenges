# Write a Python program to reverse a string.

def reverse_string(string):
    return string[::-1]


my_str = "Prashant Kumar"
print(reverse_string(my_str))


# Write a Python program to find the factorial of a number.

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(4))


# Write a Python program to check if a string is a palindrome.

def is_palindrome(my_string):
    return my_string == my_string[::-1]


print(is_palindrome("Prashant"))



