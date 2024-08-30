from sys import stdin  

c = stdin.readline().strip()
N = int(stdin.readline().strip())
ans = 0
for _ in range(N):
    tmp = stdin.readline().strip()
    if c[:5] == tmp[:5]:
        ans+=1


print(ans)
