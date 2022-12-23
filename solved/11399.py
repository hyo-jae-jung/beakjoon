import sys

N = int(sys.stdin.readline().strip())
nums = map(int,sys.stdin.readline().strip().split())
print(sum([i*j for i,j in zip(sorted(nums),reversed(range(1,N+1)))]))
