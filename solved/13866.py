from sys import stdin 

nums = list(map(int,stdin.readline().strip().split()))

nums.sort()

print(abs(nums[0]+nums[-1]-nums[1]-nums[-2]))
