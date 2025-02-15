import sys

N,K = map(int,sys.stdin.readline().strip().split())

MOD = 10**9
arr = [[i if j==1 else 1 if i==1 else 0 for i in range(K+1)] for j in range(N+1)]

for i in range(2,N+1):
    for j in range(2,K+1):
        arr[i][j] = (arr[i-1][j] + arr[i][j-1])%MOD

print(arr[N][K])
