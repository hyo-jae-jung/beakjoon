def solution(arr):
    while len(arr) > 1:
        tmp = []
        for i in range(1,len(arr)):
            tmp.append(arr[i]+arr[i-1])
        arr = tmp
    return arr[0]

from sys import stdin  
from itertools import permutations as perm

N,F = map(int,stdin.readline().strip().split())
p = perm(range(1,N+1),N)

while True:
    t = next(p)
    if F == solution(t):
        break

print(*t)
