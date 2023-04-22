from sys import stdin 
from collections import defaultdict

n = int(stdin.readline().strip())
a,b = map(int,stdin.readline().strip().split())
m = int(stdin.readline().strip())

chart = defaultdict(list)

for _ in range(m):
    i,j = map(int,stdin.readline().strip().split())
    chart[i].append(j)
    chart[j].append(i)
    
memo = [True]*(n+1)

answer = []

def check_chonsoo(n,cnt=0):
    if n == b:
        answer.append(cnt)
        return 

    if memo[n]:
        memo[n] = False
        for i in chart[n]: 
            if memo[i]:
                check_chonsoo(i,cnt=cnt+1)

check_chonsoo(a)

if answer:
    print(*answer)
else:
    print(-1)
    