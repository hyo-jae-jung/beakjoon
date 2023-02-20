from sys import stdin 

N,M = map(int,stdin.readline().strip().split())
nums = list(range(1,N+1))
for _ in range(M):
    i,j = [int(n)-1 for n in stdin.readline().strip().split()]
    nums[i],nums[j] = nums[j],nums[i]

print(*nums)
