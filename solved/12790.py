from sys import stdin 

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    hp,mp,at,de,dhp,dmp,dat,dde = map(int,stdin.readline().strip().split())
    s = (hp + dhp if hp + dhp >= 1 else 1) \
    + (mp*5 + 5*dmp if mp*5 + 5*dmp >= 1 else 5) \
    + (at*2 + 2*dat if at*2 + 2*dat >= 0 else 0) \
    + (de*2 + 2*dde)
    ans.append(s)

print(*ans,sep='\n')
