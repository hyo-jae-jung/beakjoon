from sys import stdin 
from collections import defaultdict

N = int(stdin.readline().strip())
friends = defaultdict(int)
for _ in range(N):
    friends[stdin.readline().strip()]+=1
answer = 0
# step1
a = friends['1/2']//2
friends['1/2']-=a*2

#step2
b = min(friends['1/4'],friends['3/4'])
friends['1/4']-=b
friends['3/4']-=b

#step3
if friends['1/4'] == 0:
    c = friends['1/2']+friends['3/4']
    friends['1/2']=0
    friends['3/4']=0
else:
    c = 0
    if friends['1/2'] == 1 and friends['1/4']>=2:
        c+=1
        friends['1/2']-=1
        friends['1/4']-=2

    if friends['1/4'] > 0:
        c+= (friends['1/4']//4) + (1 if friends['1/4']%4 > 0 else 0)
        friends['1/4'] = 0

print(a + b + c)
