from sys import stdin 
from collections import deque

N = int(stdin.readline().strip())
xy = []
for _ in range(N):
    temp = list(map(int,stdin.readline().strip().split()))
    if temp[0] != temp[1]:
        xy.append(temp)
xy.sort(key=lambda x:x[0])

xy = deque(xy)

buff = xy.popleft()
bars = deque()
while xy:
    temp = xy.popleft()

    if buff[1] < temp[1]:
        if buff[1] < temp[0]:
            bars.append(buff)
            buff = temp
        else:
            buff[1] = temp[1]
else:
    bars.append(buff)

answer = 0
for i,j in bars:
    answer+=j-i

print(answer)
