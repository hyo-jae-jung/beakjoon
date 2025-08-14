from sys import stdin   

N = int(stdin.readline().strip())
arr = [tuple(map(int,stdin.readline().strip().split())) for _ in range(N)]

arr.sort(key=lambda x:(x[0]))

ans = 0
stack = []
max_l,max_h = 0,0
for L,H in arr:
    while stack:
        if stack[-1][1] < H:
            stack.pop()
        else:
            stack.append((L,H))
            break

    if not stack:
        ans+=max_h*(L - max_l)
        stack.append((L,H))
        max_l = L
        max_h = H
else:
    l,h = stack.pop()
    while stack:
        ans+=(l - stack[-1][0])*h
        l,h = stack.pop()
    else:
        ans+=h
        
print(ans)
