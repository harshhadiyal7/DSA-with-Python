# Fibonacci sequence

# example usage: 0,1,1,2,3,5,8,13,21,34
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
# print first 10 Fibonacci numbers
for i in range(10):
    print(fibonacci(i)) 