import sys

T = int(sys.stdin.readline().strip())
ns = [int(sys.stdin.readline().strip()) for _ in range(T)]
ans = []
end = 10000

dp = [1] + [0]*end
for i in range(1,4):
    for j in range(i,end+1):
        dp[j]+=dp[j-i]

for i in ns:
    print(dp[i])
