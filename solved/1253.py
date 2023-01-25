from sys import stdin 

N = int(stdin.readline().strip())
nums = [int(i) for i in stdin.readline().strip().split()]

nums.sort()

cnt=0
for idx in range(len(nums)):
    i=0
    j=len(nums)-1
    good = nums[idx]
    while True:
        if idx == i:
            i+=1
        elif idx == j:
            j-=1

        if i >= j:
            break
        else:
            if nums[i]+nums[j] == good:
                cnt+=1
                break
            elif nums[i]+nums[j] > good:
                j-=1
            else:
                i+=1

print(cnt)
