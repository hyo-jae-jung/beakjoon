from sys import stdin  

t = int(stdin.readline().strip())
ans = []
for _ in range(t):
    _ = stdin.readline().strip()
    arr = list(map(int,stdin.readline().strip().split()))
    ans.append((max(arr)-min(arr))*2)

print(*ans,sep='\n')
