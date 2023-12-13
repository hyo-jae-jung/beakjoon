from sys import stdin 

B = int(stdin.readline().strip())
nums = [0] + list(map(int,stdin.readline().strip().split()))

ans = []
for i in range(1,B+1):
    ans.append(i*nums[i]-(i-1)*nums[i-1])

print(*ans)
