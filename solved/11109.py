from sys import stdin  

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    d,n,s,p = map(int,stdin.readline().strip().split())
    ns = n*s
    dnp = d+n*p
    if ns > dnp:
        ans.append("parallelize")
    elif ns < dnp:
        ans.append("do not parallelize")
    else:
        ans.append("does not matter")

print(*ans,sep='\n')
