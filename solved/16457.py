from sys import stdin   
from itertools import combinations as combi 

n,m,k = map(int,stdin.readline().strip().split())
quests = []
for _ in range(m):    
    quests.append(sum(map(lambda x: 1 << int(x),stdin.readline().strip().split())))

ans = 0
for c in combi(range(1,n*2+1),n):
    cnt = 0
    val = sum(map(lambda x:1 << x,c))
    for quest in quests:
        if val & quest == quest:
            cnt+=1
    ans = max(ans,cnt)

print(ans)
