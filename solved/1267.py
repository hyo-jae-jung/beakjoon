from sys import stdin 

N = int(stdin.readline().strip())
used_time = map(int,stdin.readline().strip().split())

def y(x):
    return (x//30 + (1 if x%30 > 0 else 0))*10

def m(x):
    return (x//60 + (1 if x%60 > 0 else 0))*15

Y,M = 0,0
for i in used_time:
    Y+=y(i+1)
    M+=m(i+1)

if Y < M:
    print('Y',Y)
elif Y > M:
    print('M',M)
else:
    print('Y','M',Y)
