from sys import stdin 
from collections import defaultdict

d = defaultdict(int)

while tree:=stdin.readline().strip():
    d[tree]+=1

answer = []
for i,j in d.items():
    answer.append((i,(j/sum(d.values()))*100))

answer.sort(key=lambda x:x[0])

for i,j in answer:
    print(f'{i} {j:.4f}')
