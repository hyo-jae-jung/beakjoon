from sys import stdin 

T = int(stdin.readline().strip())

ans =[]
for _ in range(T):
    N,M = map(int,stdin.readline().strip().split())
    ans.append((M*2 - N,N - M))

for i in ans:
    print(*i)
