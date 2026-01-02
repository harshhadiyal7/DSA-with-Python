# This is program for Count a digits.

'''
Logic:
count = 0
num = 5873
    c+=1.......(1)

n//10  --> 587
    c+=1.......(2)

n//10  --> 58
    c+=1.......(3)
    
n//10  --> 5
    c+=1.......(4)

n//10  --> 0
    stop
'''
#code  Method 1:
n=5873

num = n
count = 0
while num > 0:
    count += 1
    num //= 10
    
print("1. Count of digits:", count)
# Output: Count of digits: 4




#code Method 2: log method

'''
Logic:
log10(5487) = 3.7395 + 1 = 4.7395
'''

from math import*

n=58735
num = n
def count_digits(num):
    return int(log10(num) + 1)
print("2. Count of digits:", count_digits(num))
# Output: Count of digits: 5


#TC and SC:
'''
TC: O(log10(N)).
SC: O(1).(because we are using only constant space.)
'''