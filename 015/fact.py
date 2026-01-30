# Find factorial of a number using functional recursion.

'''
Concept: Factorial of a number n is defined as the product of all positive integers less than or equal to n.

'''
def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)
n = int(input("Enter a number: "))
print(factorial(n))