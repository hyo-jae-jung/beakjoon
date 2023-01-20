from sys import stdin 

n = int(stdin.readline().strip())
nums = [int(i) for i in stdin.readline().strip().split()]
x = int(stdin.readline().strip())

nums.sort()
l = 0
r = len(nums)-1
cnt = 0
while l < r:
    if nums[l]+nums[r] == x:
        cnt+=1
        l+=1
    elif nums[l]+nums[r] > x:
        r-=1
    elif nums[l]+nums[r] < x:
        l+=1

print(cnt)
