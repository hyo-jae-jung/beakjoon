from sys import stdin 
from itertools import combinations as comb 
from collections import defaultdict

n = int(stdin.readline().strip())
tmp,db = [],[]
d = defaultdict(int)
for _ in range(n):
    tmp.extend(list(comb([i for i,j in enumerate(stdin.readline().strip().split(),1) if j=="1"],2)))

for i in tmp:
    d[i]+=1

for key,value in d.items():
    db.append((value,key))

db.sort(key=lambda x:-x[0])

ans = [0]*5
try:
    for i in db[0][1]:
        ans[i-1] = 1

    print(db[0][0])
    print(*ans)
except:
    print(0)
    print("1 1 0 0 0")
    