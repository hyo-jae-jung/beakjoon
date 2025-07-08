from sys import stdin  

N = int(stdin.readline().strip())
K = int(stdin.readline().strip())
ans = []
n = N//2 + (1 if N%2 > 0 else 0)
for _ in range(K):
    a,b = map(int,stdin.readline().strip().split())
    if a > n:
        a = N - a + 1
    if b > n:
        b = N - b + 1
    
    xy = min(a,b)
    ans.append(xy%3 if xy%3 > 0 else 3)

print(*ans,sep='\n')
