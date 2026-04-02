from sys import stdin 
from collections import deque 

t = int(stdin.readline().strip())
ans = []
for _ in range(t):
    n = int(stdin.readline().strip())
    sanggun_home = tuple(map(int,stdin.readline().strip().split()))
    convenient_stores = deque()
    for _ in range(n):
        convenient_stores.append(tuple(map(int,stdin.readline().strip().split())))
    pentaport = tuple(map(int,stdin.readline().strip().split()))
    convenient_stores.append(pentaport)

    queue = deque([sanggun_home])
    while queue:
        x,y = queue.popleft()

        if x == pentaport[0] and y == pentaport[1]:
            ans.append('happy')
            break
        
        tmp = deque()
        while convenient_stores:
            dx,dy = convenient_stores.popleft()
            if abs(x-dx)+abs(y-dy) <= 1000:
                queue.append((dx,dy))
            else:
                tmp.append((dx,dy))
        else:
            convenient_stores = tmp
    else:
        ans.append('sad')
    
print(*ans,sep='\n')
