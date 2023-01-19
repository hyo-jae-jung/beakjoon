from sys import stdin 
from collections import deque 

inp = stdin.readline().strip()
a = 'AAAA'
b = 'BB'
x = [i for i in inp.split('.') if i]
dot = deque([i for i in inp.split('X') if i])
poly = deque([])
answer = ''
for i in x:
    if len(i)%4 not in [0,2]:
        answer = -1
        break
    else:
        poly.append(a*(len(i)//4)+b*bool(len(i)%4))
else:
    if inp[0] != '.':      
        i = 0
    else:
        i = 1
    while poly or dot:
        if i%2 == 0:
            answer+=poly.popleft()
        else:
            answer+=dot.popleft()
        i+=1

print(answer)
