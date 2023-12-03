from sys import stdin 

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    nums = list(map(int,stdin.readline().strip().split()))
    nums.sort()
    if nums[3] - nums[1] >= 4:
        ans.append('KIN')
    else:
        ans.append(sum(nums[1:4]))

print(*ans,sep='\n')
