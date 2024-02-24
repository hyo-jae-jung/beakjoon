from sys import stdin 

N = int(stdin.readline().strip())

nums = []
for _ in range(N):
    nums.append(int(stdin.readline().strip()))

diff = nums[1] - nums[0]
div = nums[1]/nums[0]

for i in range(2,len(nums)):
    if nums[i] - nums[i-1] == diff and nums[i]/nums[i-1] == div:
       diff = nums[i] - nums[i-1] 
       div = nums[i]/nums[i-1] 

    elif nums[i] - nums[i-1] != diff:
        print(int(nums[-1]*div))
        break

    elif nums[i]/nums[i-1] != div:
        print(int(nums[-1] + diff))
        break
