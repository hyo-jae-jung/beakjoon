from sys import stdin  
from itertools import permutations as perm

N = int(stdin.readline().strip())
arr = list(map(int,stdin.readline().strip().split()))

for i in perm(range(1,N+1)):
    for j in range(N):
        cnt = 0
        for k in range(j):
            if i[k] > i[j]:
                cnt+=1
        if arr[i[j]-1] != cnt:
            break
    else:
        print(*i)
        break

