from sys import stdin   
from bisect import bisect_left

N,K = map(int,stdin.readline().strip().split())
X = sorted([int(stdin.readline().strip()) for _ in range(N)])

left = 1
right = X[-1] + K

while left < right:
    mid = (left+right)//2 + (1 if (left+right)%2 > 0 else 0)

    tmp = 0
    for i in range(bisect_left(X,mid)):
        tmp+=mid-X[i]

    if tmp <= K:
        left = mid
    else:
        right = mid - 1

print(left)
