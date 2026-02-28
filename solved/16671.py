from sys import stdin 

n,k = map(int,stdin.readline().strip().split())
A = list(map(int,stdin.readline().strip().split()))
B = list(map(int,stdin.readline().strip().split()))

AB = []
for a,b in zip(A,B):
    AB.append((a,b))
AB.sort(key=lambda x:x[1])

rest_idlers = []
occupied_jobs = set()
for i in range(n):
    a,b = AB.pop()
    if a not in occupied_jobs:
        occupied_jobs.add(a)
    else:
        rest_idlers.append(b)

ans = 0
for _ in range(k - len(occupied_jobs)):
    ans+=rest_idlers.pop()

print(ans)
