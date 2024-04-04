from sys import stdin 

N = int(stdin.readline().strip())
ans = 0
t = 30
for j in range(N):
    if t <= 0:
        t = 30
    i = int(stdin.readline().strip()) 
    if 2*t >= i:
        ans+=1
    t-= i

print(ans)
