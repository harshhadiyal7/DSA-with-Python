# Extract of Digits

#Logic
'''
num=n
while num>0:
    
    last_digit=num%10
    print(last_digit)
    num=num//10
'''

# Reverse gigits
#  5 8 7 3 -> 3 7 8 5
n=5873

num = n
digits = []
while num > 0:
    d = num % 10
    
    if d != 0:
        digits.append(d)

    num //= 10

print(*digits)

# Output: 3 7 8 5
