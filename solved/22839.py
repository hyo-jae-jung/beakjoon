from sys import stdin  

ans = []
while (a:=int(stdin.readline().strip())) != 0:
    dp = [1] + [0]*a

    for i in range(1,int(a**0.5)+1):
        for j in range(i**2,a+1):
            dp[j]+=dp[j-i**2]

    ans.append(dp[-1])

print(*ans,sep='\n')
