from sys import stdin 

N,M = map(int,stdin.readline().strip().split())
nums = list(range(1,N+1))
for _ in range(M):
    i,j = [int(i) for i in stdin.readline().strip().split()]
    for k in range(j-i):
        a = i-1+k
        b = j-1-k
        if a <= b:
            nums[a],nums[b] = nums[b],nums[a]

print(*nums)
