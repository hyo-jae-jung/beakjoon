from sys import stdin  

N,M = map(int,stdin.readline().strip().split())
nums = map(int,stdin.readline().strip().split())

ans = 1

for i in nums:
    ans*= i%M

print(ans%M)
