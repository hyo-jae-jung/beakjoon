from sys import stdin 

N,K = map(int,stdin.readline().strip().split())
nums = list(map(int,stdin.readline().strip().split()))

ans = []
for i,j in enumerate(range(K,N+1)):
    ans.append(sum(nums[i:j]))

print(max(ans))
