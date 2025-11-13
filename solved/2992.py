from sys import stdin  
from collections import deque

X = list(map(int,list(stdin.readline().strip())))

d = deque()
for i in range(len(X)-1,0,-1):
    d.appendleft(X[i])
    if X[i-1] < X[i]:
        break
else:
    d.appendleft(X[i-1])

if X == list(d):
    print(0)
else:
    d = sorted(d)
    for j in range(len(d)):
        if X[i-1] < d[j]:
            X[i-1],d[j] = d[j],X[i-1]
            break

    print(''.join(map(str,X[:i]+sorted(d))))
