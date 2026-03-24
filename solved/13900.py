from sys import stdin 

N = int(stdin.readline().strip())
arr = list(map(int,stdin.readline().strip().split()))
prefix_sum = [0]
for i in arr:
    prefix_sum.append(prefix_sum[-1] + i)

ans = 0
for i in range(N):
    ans+=arr[i]*(prefix_sum[-1] - prefix_sum[i+1])

print(ans)
