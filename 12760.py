from sys import stdin  
from collections import defaultdict

N,M = map(int,stdin.readline().strip().split())

arr = []
d = defaultdict(int)
for _ in range(N):
    arr.append(sorted(list(map(int,stdin.readline().strip().split()))))

for _ in range(M):
    m = -1
    for i in range(N):
        m = max(m,arr[i][-1])
            
    for i in range(N):
        if arr[i][-1] == m:
            d[i+1]+=1
        arr[i].pop()

t = sorted(d.items(),key=lambda x:(-x[1]))
print(*[i for i,j in t if t[0][1] == j])
