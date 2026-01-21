# Print sum of 1 to n using functional recursion.
def func(sum, i,n):
    if i > n:
        print(sum)
        return 
    func(sum + i, i + 1, n)
n = int(input("Enter a number: "))
func(0, 1, n)   
