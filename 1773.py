from sys import stdin 

N,C = map(int,stdin.readline().strip().split())
ans = set()
for _ in range(N):
    ans|=set(range(0,C+1,int(stdin.readline().strip())))

print(len(ans)-1)
