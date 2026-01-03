# Hashing in Python.
'''
Prestoring values into same data structure like dictionary, set and lists.
Constraints: 1. 1<= n[i] <= 10
             2. n can have 10^8 elements
             3. m can have 10^8 elements
'''
# Brute Force Approach
n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2,6,9]

for num in m:
    count = 0
    for x in n:
        if x==num:
            count += 1
    print(f"{num} : {count}")

# Optimal Approach
'''Constraints: 1. 1<= n[i] <= 10
             2. n can have 10^8 elements
             3. m can have 10^8 elements
'''
n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

hash_list = [0]*11  # Since n[i] can be from 1 to 10
for num in n:
    hash_list[num] += 1
for num in m:
    if num<1 or num>10:
        print(f"{num} : 0")
    else:
        print(f"{num} : {hash_list[num]}")
        
# Character hasing
s = "azyxyyzaaaa"
q = ["d", "a", "y", "v"]

hash_list = [0]*26  # Since we are considering only lowercase letters a-z

for ch in s:
    ascii_val = ord(ch)
    index  = ascii_val - 97  # 'a' starts from 97
    hash_list[index] += 1
for ch in q:
    ascii_val = ord(ch)
    index  = ascii_val - 97
    print(f"{ch} : {hash_list[index]}")
