from sys import stdin 
from collections import deque 

A,B = map(int,stdin.readline().strip().split())

def bfs(a,b):
    queue = deque([(a,1)])
    while queue:
        temp = queue.popleft()
        if temp[0] == b:
            return temp[1]
        if temp[0] < b:
            queue.append((temp[0]*2,temp[1]+1))
            queue.append((int(str(temp[0])+'1'),temp[1]+1))
    else:
        return -1
    
print(bfs(A,B))
