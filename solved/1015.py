from sys import stdin 
from collections import deque, defaultdict

N = int(stdin.readline().strip())
A = list(map(int,stdin.readline().strip().split()))

d = defaultdict(deque)

B = A.copy()
B.sort()

for i,j in enumerate(B):
    d[j].appendleft(i)

ans = []
for i in A:
    ans.append(d[i].pop())
    
print(*ans)
