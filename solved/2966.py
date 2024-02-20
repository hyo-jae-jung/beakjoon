from sys import stdin 
from itertools import cycle 

N = int(stdin.readline().strip())
q = stdin.readline().strip()

Adrian = ['A','B','C']
Bruno = ['B','A','B','C']
Goran = ['C','C','A','A','B','B']

scores = {
        'Adrian':0,
        'Bruno':0,
        'Goran':0,
        }

for i in range(N):
    if q[i] == Adrian[i%3]:
        scores['Adrian']+=1
    if q[i] == Bruno[i%4]:
        scores['Bruno']+=1
    if q[i] == Goran[i%6]:
        scores['Goran']+=1

ans = sorted(scores.items(),key=lambda x:(-x[1],x[0]))

max_cnt = ans[0][1]
print(max_cnt)
for i,j in ans:
    if max_cnt == j:
        print(i)
    else:
        break
    