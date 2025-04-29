from sys import stdin  

ans = []
while (i := stdin.readline().strip()) != '0 0.00':
    n,m = i.split()
    n = int(n)
    m = int(float(m)*100+0.5)

    cal,price = [],[]
    for _ in range(n):
        c,p = stdin.readline().strip().split()
        cal.append(int(c))
        price.append(int(float(p)*100+0.5))

    dp = [0]*(m+1)
    for i in range(n):
        for j in range(price[i],m+1):
            dp[j] = max(dp[j],dp[j-price[i]]+cal[i])
    
    ans.append(max(dp))

print(*ans,sep='\n')

"""
unbounded knapsack
"""
