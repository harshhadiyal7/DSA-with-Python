# Hashing in Python.
'''
Prestoring values into same data structure like dictionary, set and lists.
Constraints: 1. 1<= n[i] <= 10
             2. n can have 10^8 elements
             3. m can have 10^8 elements
'''
# Brute Force Approach
n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

for num in m:
    count = 0
    for x in n:
        if x==num:
            count += 1
    print(f"{num} : {count}")