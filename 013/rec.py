# Print x is N times.
def print_n_times(x, n):
    if n==0:
        return
    print(x)
    print_n_times(x, n - 1)
    
print_n_times("Hasrh", 5)

# Print numbers from 1 to n.
i=1
n=5
def func(i,n):
    if i>n:
        return
    print(i)
    func(i+1, n)
    
func(i,n)

# Print numbers from n to 1.
def func2(n):
    if n==0:
        return
    print(n)
    func2(n-1)
func2(5)        
