import sys
from collections import defaultdict

T = int(sys.stdin.readline().strip())
t = []
for _ in range(T):
    t.append(int(sys.stdin.readline().strip()))

t_sort = sorted(t)
t_d = defaultdict(int)

j = 0
abc = []
for i in range(1,t_sort[-1]+1):

    if i == 1:
        abc.append(1)
    elif i == 2:
        abc.append(2)
    elif i == 3:
        abc.append(4)
    else:
        abc[2],abc[1],abc[0] = sum(abc)%1000000009,abc[2],abc[1]

    if i == t_sort[j]:
        if i < 4:
            t_d[i] = abc[i-1]
        else:
            t_d[i] = abc[2]
        j+=1
        if j == len(t):
            break

for i in t:
    print(t_d[i])
    