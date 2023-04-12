from sys import stdin 
from collections import defaultdict

N,X = map(int,stdin.readline().strip().split())
blog_daily_visited_cnt = [int(i) for i in stdin.readline().strip().split()]

acum = [blog_daily_visited_cnt[0]]
for i in range(1,len(blog_daily_visited_cnt)):
    acum.append(acum[-1]+blog_daily_visited_cnt[i])
    
sum_by_section = []

for i in range(X-1,N):
    sum_by_section.append(acum[i]-(acum[i-X] if i >= X else 0))

m = max(sum_by_section)

if m == 0:
    print('SAD')
else:    
    d = defaultdict(int)
    for i in sum_by_section:
        d[i]+=1
    print(m,d[m],sep='\n')
