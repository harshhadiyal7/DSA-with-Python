# Check Armstrong number.

'''
It is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
eg: 153 = 1^3 + 5^3 + 3^3= 1+125+27 = 153
    1634 = 1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634
'''

'''
dry run:
num = 153
nod = lan(str(n))
total = 0
      = 0 + 3**3 = 27
      = 27 + 5**3 = 152
      = 152 + 1**3 = 153
      
      ld = 3 **nod
         = 3 ** 3 = 27
      ld = 5 **nod
         = 5 ** 3 = 125 
      ld = 1 **nod
         = 1 ** 3 = 1'''
         
n=153
num=n
total=0
nod=len(str(n))
while n>0:
    ld=n%10
    total=total + ld**nod
    n=n//10
if total==num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
