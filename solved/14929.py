from sys import stdin 

n = int(stdin.readline().strip())
nums = list(map(int,stdin.readline().strip().split()))

total_sum = sum(nums)
ans = 0

for i in range(len(nums)-1):
    total_sum-=nums[i]
    ans+=nums[i]*total_sum

print(ans)
