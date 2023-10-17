from sys import stdin 

N = int(stdin.readline().strip())

nums = []
for _ in range(N):
    nums.append(int(stdin.readline().strip()))

ans = 0
for i in range(N-2,-1,-1):
    if nums[i] >= nums[i+1]:
        tmp = nums[i] - nums[i+1] + 1
        ans+=tmp
        nums[i]-=tmp

print(ans)
