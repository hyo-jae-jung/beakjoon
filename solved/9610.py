from sys import stdin 
from collections import defaultdict

n = int(stdin.readline().strip())
answer = defaultdict(int)

for _ in range(n):
    x,y = map(int,stdin.readline().strip().split())
    if x == 0 or y == 0:
        answer['AXIS']+=1
    elif x > 0 and y > 0:
        answer['Q1']+=1
    elif x < 0 and y > 0:
        answer['Q2']+=1
    elif x < 0 and y < 0:
        answer['Q3']+=1
    elif x > 0 and y < 0:
        answer['Q4']+=1

names = ['Q1','Q2','Q3','Q4','AXIS']

for i in names:
    print(f'{i}: {answer[i]}')
    