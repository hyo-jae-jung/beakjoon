from sys import stdin  

N,K = map(int,stdin.readline().strip().split())
N = list(map(int,stdin.readline().strip().split()))

N.sort(reverse=True)

ans = 0
for i,j in zip(N[:K],range(K)):
    ans+=i-j

print(ans)
