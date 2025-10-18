from sys import stdin   

N = int(stdin.readline().strip())
ans = 0
stack = []
for _ in range(N):
    i = stdin.readline().strip()
    if i[0] == '1':
        _,A,T = map(int,i.split())
        stack.append((A,T))

    if stack:
        a,t = stack.pop()
        t-=1
        if t == 0:
            ans+=a
        else:
            stack.append((a,t))

print(ans)
