from sys import stdin  

N,X = map(int,stdin.readline().strip().split())
ans = -1
for _ in range(N):
    S,T = map(int,stdin.readline().strip().split())
    ans = S if sum([S,T]) <= X and ans < S else ans

print(ans)
