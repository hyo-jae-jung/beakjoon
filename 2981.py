import sys

N = int(sys.stdin.readline().strip())
nums = [int(sys.stdin.readline().strip()) for _ in range(N)]

print(set([nums[0]%i for i in range(2,nums[0]+1)]))
