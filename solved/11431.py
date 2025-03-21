from sys import stdin   

K = int(stdin.readline().strip())
ans = []
for _ in range(K):
    n,s,p = map(int,stdin.readline().strip().split())
    points = []
    for _ in range(n+1):
        x,y = map(int,stdin.readline().strip().split())
        points.append((x,y))
    l = 0
    for i in range(1,n+1):
        l+=max(abs(points[i][0]-points[i-1][0]),abs(points[i][1]-points[i-1][1]))

    ans.append(s*l//p + (1 if s*l%p > 0 else 0))

for i in range(K):
    print(f"Data Set {i+1}:")
    print(ans[i])
    print()
