from sys import stdin 

N,K = map(int,stdin.readline().strip().split())
T = sorted(list(map(int,stdin.readline().strip().split())))

ans = 0
pre_val = 0
for i in range(K):
    s,r = i//2,i%2
    if r == 0:
        ans+=T[-(s+1)] - pre_val
    else:
        pre_val = T[s]

print(ans)
