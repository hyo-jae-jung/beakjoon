from sys import stdin  

N,M,H = map(int,stdin.readline().strip().split())
students = []
for _ in range(N):
    students.append(list(map(int,stdin.readline().strip().split())))

dp = [1] + [0]*H
for blocks in students:
    tmp_dp = dp.copy()
    for block in blocks:
        for h in range(H,block-1,-1):
            tmp_dp[h]+=dp[h-block]%10007
    dp = tmp_dp

print(dp[H]%10007)
