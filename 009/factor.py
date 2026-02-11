# Print all factors of a number.
'''
10 [1, 2, 5, 10]
15 [1, 3, 5, 15]
25 [1, 5, 25]
7 [1, 7]
19 [1, 19]
'''
# 1. Brute Force solution
'''
n=20
20[1, 2, 4, 5, 10, 20]
Time Complexity: O(n)
Space Complexity: O(K) where K is number of factors.
'''
n=20
result = []
num = n
for i in range(1, num + 1):
    if num % i == 0:
        result.append(i)

print(result)      

# 2. Better solution
'''
    We can see that after 1/2 of n, no factors will be there except n itself.
    n=10
    10[1, 2, 5, 10]
    Time Complexity: O(N/2)= O(N)
    Space Complexity: O(K) where K is number of factors.
'''

n=20
num = n
result = []
for i in range(1, num//2 + 1):
    if num % i == 0:
        result.append(i)
result.append(num)
print(result)

# 3. Optimal solution

'''
    We can see that factors are in pairs.
    n=36
    36[1--->36, 
       2--->18,
       3--->12, 
       4--->9, 
       6--->6]'''
       
from math import sqrt
n=36
num = n
result = []
for i in range(1, int(sqrt(num)) + 1):
    if num%i == 0:
        result.append(i)
        if i != num // i:
            result.append(num // i)

print(sorted(result))   
# Time Complexity: O(sqrt(n))
# Space Complexity: O(K) where K is number of factors.
