# Find factorial of a number using functional recursion.
def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)
n = int(input("Enter a number: "))
print(factorial(n))