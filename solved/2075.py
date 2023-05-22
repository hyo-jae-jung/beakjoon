from sys import stdin 
from heapq import nlargest

N = int(stdin.readline().strip())

arr = list(map(int,stdin.readline().strip().split()))
for _ in range(N-1):
    arr+=list(map(int,stdin.readline().strip().split()))
    arr = nlargest(N,arr)

print(min(arr))
