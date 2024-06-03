from sys import stdin  

N,M,K = map(int,stdin.readline().strip().split())
ans = [-1]
i = 0
max_damage = 0
for _ in range(M):
    t,r = map(int,stdin.readline().strip().split())
    i+=1
    max_damage+=r
    if ans[0] == -1 and max_damage > K:
        ans = [i,1]

print(*ans)
