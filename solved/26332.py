from sys import stdin   

n = int(stdin.readline().strip())
ans = []
for _ in range(n):
    c,p = map(int,stdin.readline().strip().split())
    ans.append(f"{c} {p}\n{(p-2)*(c-1) + p}")

print(*ans,sep='\n')
