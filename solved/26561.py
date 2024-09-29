from sys import stdin

n = int(stdin.readline().strip())

ans = []
for _ in range(n):
    p,t = map(int,stdin.readline().strip().split())
    ans.append(p + t//4 - t//7)
    
print(*ans,sep='\n')
