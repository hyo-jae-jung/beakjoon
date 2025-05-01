from sys import stdin  

_ = int(stdin.readline().strip())
weight = list(map(int,stdin.readline().strip().split()))
_ = int(stdin.readline().strip())
check = list(map(int,stdin.readline().strip().split()))

dp = [0]*40000 + [1] + [0]*40000

for i in weight:
    tmp_dp_left = dp.copy()
    tmp_dp_right = dp.copy()
    for j in range(80000,i-1,-1):
        tmp_dp_right[j]+=dp[j-i]
    for j in range(80000-i+1):
        tmp_dp_left[j]+=dp[j+i]
    for i in range(80001):
        dp[i] = max(tmp_dp_left[i],tmp_dp_right[i])
        
ans = []
for i in check:
    ans.append('Y' if dp[i+40000] > 0 else 'N')

print(*ans)
