from sys import stdin  
from collections import Counter  

N,_ = map(int,stdin.readline().strip().split())
ans = 0
for _ in range(N):
    if max(t:=Counter(list(stdin.readline().strip())),key=t.get) == "O":
        ans+=1

print(ans)
