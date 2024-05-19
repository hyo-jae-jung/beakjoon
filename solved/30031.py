from sys import stdin  

N = int(stdin.readline().strip())
d = {136:1000,142:5000,148:10000,154:50000}

ans = 0
for _ in range(N):
    w,_ = map(int,stdin.readline().strip().split())
    ans+=d[w]

print(ans)
