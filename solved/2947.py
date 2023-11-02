from sys import stdin 

nums = list(map(int,stdin.readline().strip().split()))

i = 0
while nums != [1,2,3,4,5]:
    if nums[i] > nums[i+1]:
        nums[i],nums[i+1] = nums[i+1],nums[i]
        print(*nums)
    
    if i < 3:
        i+=1
    else:
        i=0
