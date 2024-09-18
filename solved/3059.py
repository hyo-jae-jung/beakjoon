from sys import stdin  


T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    S = stdin.readline().strip()
    total_val = 2015
    g = set()
    for i in S:
        if i not in g:
            total_val-=ord(i)
            g.add(i)

    ans.append(total_val)

print(*ans,sep='\n')
