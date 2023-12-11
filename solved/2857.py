from sys import stdin 
import re

p = re.compile('FBI')

names = []
for _ in range(5):
    names.append(stdin.readline().strip())

ans = []
for i,j in enumerate(names,1):
    if bool(p.search(j)):
        ans.append(i)

if ans:
    print(*ans)
else:
    print('HE GOT AWAY!')
