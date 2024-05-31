from sys import stdin  

N = int(stdin.readline().strip())

ans = 0
l = []
for _ in range(N):
    l.append(list(map(int,stdin.readline().strip().split())))

l.sort(key=lambda x:(-x[0],x[1]))

for i in range(5,N):
    if l[i][0] == l[4][0]:
        ans+=1
    else:
        break

print(ans)
