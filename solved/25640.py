from sys import stdin 

jinho = stdin.readline().strip()
N = int(stdin.readline().strip())
ans = 0
for _ in range(N):
    if jinho == stdin.readline().strip():
        ans+=1

print(ans)
