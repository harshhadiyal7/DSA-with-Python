# Check given string is palindrome or not.

#Method 1 (Using Loop)

s="nitin"
n=len(s)
left=0
right=n-1

while left < right:
    if s[left]!=s[right]:
        print("Not a Palindrome")
        break
    left+=1
    right-=1
else:
    print("Palindrome")
    
#Method 2 (Using Recursion)

s="madam"
def func(s, left, right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return func(s, left + 1, right - 1)
print(func(s, 0, len(s) - 1))
