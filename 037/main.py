#Best Time to Buy and Sell Stock(leetcode 121).
'''
prise = [7,2,1,5,6,4,8]
we find lowest price to buy, and highest price to sell and return meximum profit.
'''
#Brute force solution
prise = [7,2,1,5,6,4,8]
n=len(prise)
max_profit=0

for i in range (0, n):
    for j in range(i+1, n):
        if prise[j] > prise[i]:
            p= prise[j]-prise[i]
            if p > max_profit:
                max_profit = p

print(f"The maximum profit is: {max_profit}")
'''
TC : O(n^2)
SC : O(1)
'''
