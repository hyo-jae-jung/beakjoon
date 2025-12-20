from sys import stdin   

N = int(stdin.readline().strip())
arr = list(map(int,stdin.readline().strip().split()))
dp = [[0]*21 for i in range(N-1)]
dp[0][arr[0]] = 1

for i in range(1,N-1):
    for j in range(21):
        if dp[i-1][j] > 0:
            if j+arr[i] <= 20:
                dp[i][j+arr[i]]+=dp[i-1][j]
            if j-arr[i] >= 0:
                dp[i][j-arr[i]]+=dp[i-1][j]

print(dp[-1][arr[-1]])
