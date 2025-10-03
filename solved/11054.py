from sys import stdin   

N = int(stdin.readline().strip())
A = list(map(int,stdin.readline().strip().split()))

dp_large = [1]*N
dp_small = [1]*N

for i in range(1,N):
    tmp = 0
    for j in range(i-1,-1,-1):
        if A[i] > A[j]:
            tmp = max(tmp,dp_large[j])
    dp_large[i]+=tmp

for i in range(N-1-1,-1,-1):
    tmp = 0
    for j in range(i,N):
        if A[i] > A[j]:
            tmp = max(tmp,dp_small[j])
    dp_small[i]+=tmp

ans = 0
for i in range(N):
    ans = max(ans, dp_large[i] + dp_small[i] - 1)

print(ans)
