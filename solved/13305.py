from sys import stdin
from collections import deque

N = int(stdin.readline().strip())
distance = deque(map(int,stdin.readline().strip().split()))
city = deque(map(int,stdin.readline().strip().split()))
min_cost = 0
km = 0 
i = 1
while distance:

    km+=distance.popleft()

    if city[0] > city[i]:

        min_cost+=km*city.popleft()
        for _ in range(i-1):
            city.popleft()
        km=0
        i=1
    elif city[0] <= city[i]:
        i+=1
else:
    min_cost+=city[0]*km

print(min_cost)
