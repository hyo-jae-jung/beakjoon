from sys import stdin  
from heapq import heapify,heappop

N = int(stdin.readline().strip())
A = list(map(int,stdin.readline().strip().split()))
C = list(map(int,stdin.readline().strip().split()))
D = A.copy()
D.sort()
dd = {}

for i in range(N):
    dd.update({D[i]:i+1})

for i in range(N):
    A[i] = dd[A[i]]
    C[i] = dd[C[i]]

del dd, D

def main():

    if A == C:
        return 1

    global N
    d = {}
    for i in range(N):
        d.update({A[i]:i})

    B = A.copy()
    B = list(map(lambda x:-x,B))
    heapify(B)

    for i in range(N-1,-1,-1):
        max_idx = d[-heappop(B)]

        if i != max_idx:
            d[A[max_idx]] = i
            d[A[i]] = max_idx
            A[max_idx],A[i] = A[i],A[max_idx]

        if A == C:
            return 1   

    return 0

print(main())
