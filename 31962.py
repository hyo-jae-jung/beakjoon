from sys import stdin  

N,X = map(int,stdin.readline().strip().split())
ans = [-1]
for _ in range(N):
    S,T = map(int,stdin.readline().strip().split())
    ans = [S,T] if sum([S,T]) > sum(ans)  and sum([S,T]) <= X else ans

print(ans[0])
