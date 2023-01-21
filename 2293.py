from sys import stdin 

n,k = map(int,stdin.readline().strip().split())
nums = []

for _ in range(n):
    temp = int(stdin.readline().strip())
    nums+=[temp]*(k//temp)

left = 0
right = 0
cnt = 0
hab = 0
while right <= len(nums):
    if hab == k:
        cnt+=1
        hab-=nums[left]
        left+=1
