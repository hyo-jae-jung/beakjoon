from sys import stdin  

H,x = map(int,stdin.readline().strip().split())
ans = 0
X = 1
for _ in range(H):
    X = (X*x)%(10**9+7)
    ans = (ans%(10**9+7) + (int(stdin.readline().strip())*X)%(10**9+7))%(10**9+7)

print(ans%(10**9+7))
