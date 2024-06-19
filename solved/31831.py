from sys import stdin  

N,M = map(int,stdin.readline().strip().split())
A = list(map(int,stdin.readline().strip().split()))

ans = 0
acc = 0
for i in A:
    acc = acc+i if acc+i >= 0 else 0
    if acc >= M:
        ans+=1

print(ans)
