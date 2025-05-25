from sys import stdin  

N = int(stdin.readline().strip())

Ns = N*(N+1)//2

if Ns%2 == 1:
    print(0)
else:
    dp = [1] + [0]*(Ns//2)
    for i in range(1,N+1):
        for j in range(Ns//2,i-1,-1):
            dp[j]+=dp[j-i]

    print(dp[-1]//2)
