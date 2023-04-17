from sys import stdin 

N = int(stdin.readline().strip())
budget_demand = [int(i) for i in stdin.readline().strip().split()]
budget_limit = int(stdin.readline().strip())

left = 0
right = max(budget_demand)

while left <= right:
    mid = (left+right)//2
    distribution = sum(i if i < mid else mid for i in budget_demand)
    if distribution <= budget_limit:
        left = mid + 1
    else:
        right = mid - 1
        
print(right)
