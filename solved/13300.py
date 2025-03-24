from sys import stdin    

N,K = map(int,stdin.readline().strip().split())
d = {}
for _ in range(N):
    s = stdin.readline().strip()
    if d.get(s):
        d[s]+=1
    else:
        d.update({s:1})

ans = 0
for i in d.values():
    ans+= i//K + (1 if i%K > 0 else 0)

print(ans)
