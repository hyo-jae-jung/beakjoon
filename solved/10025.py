from sys import stdin  

N,K = map(int,stdin.readline().strip().split())
X = [0]*(1_000_001)
min_x = 1000002
max_x = -1
for _ in range(N):
    g,x = map(int,stdin.readline().strip().split())
    X[x] = g
    min_x = min(x,min_x)
    max_x = max(x,max_x)

ans = 0

if 2*K + 1 >= max_x - min_x + 1:
    ans = sum(X)
else:
    prefix_sum = [0]
    for i in range(max_x + 1):
        prefix_sum.append(prefix_sum[-1] + X[i])
    
    for i in range(2*K + 1,max_x + 2):
        ans = max(ans,prefix_sum[i] - prefix_sum[i - (2*K + 1)])

print(ans)
