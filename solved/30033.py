from sys import stdin 

N = int(stdin.readline().strip())
plan = list(map(int,stdin.readline().strip().split()))
action = list(map(int,stdin.readline().strip().split()))
ans = 0
for i in range(N):
    if plan[i] <= action[i]:
        ans+=1

print(ans)
