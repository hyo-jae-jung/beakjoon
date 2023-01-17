from sys import stdin 

N,M = map(int,stdin.readline().strip().split())
nums = [int(i) for i in stdin.readline().strip().split()]+[0]

left = 0
right = 0
cnt = 0
hab = 0
answer = []
while right < len(nums):
    if hab == M:
        cnt+=1
        hab-=nums[left]
        left+=1
    elif hab < M:
        hab+=nums[right]
        right+=1
    elif hab > M:
        hab-=nums[left]
        left+=1

print(cnt)
