from sys import stdin   

N,M = map(int,stdin.readline().strip().split())
K = list(map(int,stdin.readline().strip().split()))

ans = 0
for i in range(2,N+1):
    for j in K:
        if i%j == 0:
            ans+=i
            break

print(ans)
