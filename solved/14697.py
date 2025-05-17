from sys import stdin  

A,B,C,N = map(int,stdin.readline().strip().split())

dp = [1] + [0]*N
for room in [A,B,C]:
    for i in range(room,N+1):
        if dp[i-room] == 1:
            dp[i] = 1 
    print(*dp)

print(dp[N])
