from sys import stdin 

N,X = map(int,stdin.readline().strip().split())
A = list(map(int,stdin.readline().strip().split()))

ans = 1000*X*2+1
for i in range(1,N):
    ans = min(ans,(A[i]+A[i-1])*X)

print(ans)
