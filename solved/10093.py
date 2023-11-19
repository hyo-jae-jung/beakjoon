from sys import stdin 

nums = list(map(int,stdin.readline().strip().split()))

A,B = min(nums),max(nums)
print(B-A-1 if B > A else 0)
print(*range(A+1,B))
