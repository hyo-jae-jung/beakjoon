from sys import stdin  

n,m = map(int,stdin.readline().strip().split())
T = list(map(int,stdin.readline().strip().split()))
perfix_sum = [0]
for i in range(n):
    perfix_sum.append(T[i] + perfix_sum[-1])

ans = 0
for i in range(m,n+1):
    ans = max(ans,perfix_sum[i] - perfix_sum[i - m])

print(ans)
