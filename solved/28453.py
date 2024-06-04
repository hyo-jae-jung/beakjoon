from sys import stdin  

_ = stdin.readline().strip()
levs = stdin.readline().strip().split()

ans = []
for i in levs:
    if int(i) >= 300:
        ans.append(1)
    elif int(i) >= 275:
        ans.append(2)
    elif int(i) >= 250:
        ans.append(3)
    else:
        ans.append(4)

print(*ans)
