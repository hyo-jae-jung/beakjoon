from sys import stdin  
from heapq import heapify,heappop

ans = []
while (t:=stdin.readline().strip()) != '0 0':
    a0,L = t.split()
    L = int(L)
    a0 = a0.zfill(L)
    h = list(a0)
    heapify(h)

    A = [int(a0)]

    while True:

        M,m = '',''
        while h:
            t = heappop(h)
            M = t + M
            m = m + t
        ai = int(M) - int(m)
        if ai in A:
            break
        A.append(ai)
        h = list(str(ai).zfill(L))
        heapify(h)

    I = len(A)
    J = 0
    for i in range(len(A)):
        if A[i] == ai:
            J = i
            break
    ans.append((J,ai,I-J))

for i in ans:
    print(*i)
