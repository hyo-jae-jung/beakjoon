from sys import stdin  

n = int(stdin.readline().strip())
d = {}
for _ in range(n):
    tmp = stdin.readline().strip()
    if d.get(tmp):
        d[tmp]+=1
    else:
        d.update({tmp:1})

print(*sorted(list(d.items()),key=lambda x:(x[1],x[0]))[-1])
