from sys import stdin 
from collections import defaultdict 


N = int(stdin.readline().strip())
nums = map(int,stdin.readline().strip().split())
words = stdin.readline().strip()

d = {}
d[0]=' '
for i in range(0,52):
    if i < 26:
        n=i
    else:
        n=i+6
    d[i+1]=chr(65+n)

password = defaultdict(int)

for i in nums:
    password[d[i]]+=1

for i in words:
    password[i]-=1
    if password[i] < 0:
        print('n')
        break 
else:
    print('y')
