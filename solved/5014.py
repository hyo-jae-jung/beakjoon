from sys import stdin 
from collections import deque 

F,S,G,U,D = map(int,stdin.readline().strip().split())

floor_cnt = [1e6+1]*(F+1)
queue = deque([[S,0]])

while queue:
    temp = queue.popleft()
    if temp[0] == G:
        print(temp[1])
        break

    if floor_cnt[temp[0]] > temp[1]:
        floor_cnt[temp[0]] = temp[1]
        if temp[0]+U <= F:
            queue.append([temp[0]+U,temp[1]+1])
        if temp[0]-D >= 1:
            queue.append([temp[0]-D,temp[1]+1])
else:
    print("use the stairs")
