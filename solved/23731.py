from sys import stdin   

N = int(stdin.readline().strip())
l = len(str(N))
ans = int(N)

for i in range(l):
    t = int(str(N)[l-i-1])
    if t >= 5:
        N+=(10-t)*(10**i)
    else:
        N-=(t*(10**i))
    ans=max(ans,N)

print(ans)
