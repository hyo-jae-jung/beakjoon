from sys import stdin  

N = int(stdin.readline().strip())
ans = []
for _ in range(N):
    d = stdin.readline().strip()
    if d[len(d)//2]==d[len(d)//2-1]:
        ans.append("Do-it")
    else:
        ans.append("Do-it-Not")

print(*ans,sep='\n')
