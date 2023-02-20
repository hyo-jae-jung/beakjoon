from sys import stdin 

N,M = map(int,stdin.readline().strip().split())
nums = [0]*N
for _ in range(M):
    i,j,k = [int(n) for n in stdin.readline().strip().split()]
    for l in range(i-1,j):
        nums[l] = k

print(*nums)
