from sys import stdin  

N = int(stdin.readline().strip())
A = list(map(int,stdin.readline().strip().split()))
dp = A.copy()

for i in range(1,N):
    tmp = 0
    for j in range(i-1,-1,-1):
        if A[i] > A[j]:
            tmp = max(dp[j],tmp)
    else:
        dp[i]+=tmp

print(max(dp))
