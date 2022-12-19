import sys

N = int(sys.stdin.readline().strip())
nums = sorted(list(map(int,sys.stdin.readline().strip().split())))

if N%2 == 0:
    print(nums[0]*nums[-1])
else:
    print(nums[int(len(nums)/2)]**2)
