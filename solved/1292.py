from sys import stdin 
A,B = map(int,stdin.readline().strip().split())

nums = [1]
while len(nums) < B:
    temp = nums[-1]+1
    nums.extend([temp]*temp)

print(sum(nums[A-1:B]))
