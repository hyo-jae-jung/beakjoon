from sys import stdin  

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    s = set()
    n = int(stdin.readline().strip())
    for _ in range(n):
        s.add(stdin.readline().strip())

    ans.append(len(s))

print(*ans,sep='\n')
