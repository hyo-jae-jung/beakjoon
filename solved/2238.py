from sys import stdin  
from collections import defaultdict

U,N = map(int,stdin.readline().strip().split())
db = []
cnt = defaultdict(int)
for _ in range(N):
    name,price = stdin.readline().strip().split()
    db.append((name,int(price)))
    cnt[int(price)]+=1

min_price = sorted(cnt.items(),key=lambda x:(x[1],x[0]))[0][0]

for i,j in db:
    if j == min_price:
        print(i,j)
        break

