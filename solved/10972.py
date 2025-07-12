from sys import stdin
from heapq import heappop,heappush

N = int(stdin.readline().strip())
arr = list(map(int,stdin.readline().strip().split()))

def next_permutation(arr):
    h = []
    while len(arr) > 1:
        b = arr.pop()
        heappush(h,b)
        if arr[-1] < b:
            tmp = []
            c = arr.pop()
            while h:
                d = heappop(h)
                if d > c:
                    arr.append(d)
                    tmp.append(c)
                    c = N+1
                else:
                    tmp.append(d)
            return arr + tmp
    return [-1]

print(*next_permutation(arr))
