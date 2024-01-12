from sys import stdin 

n = stdin.readline().strip()
ans = 0
for i in n:
    ans+=int(i)**5

print(ans)
