# Check Palindrome number.

''''
Palindrome number is a number that remains the same when its digits are reversed. 
For example:
121 is a palindrome, while 123 is not.
    '''

n = 256
num = n
result = 0
while num > 0:
    ld = num % 10
    result = (result * 10) + ld
    num = num // 10
if n == result:
    print(f"{n} is a Palindrome number")
else:
    print(f"{n} is not a Palindrome number")
