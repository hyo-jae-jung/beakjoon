from sys import stdin 
from collections import defaultdict 

x = stdin.readline().strip()

def F(x):
    return str(int(x[0])*len(x))

d = defaultdict(bool)

while True:
    x1 = F(x)
    if x1 == x:
        print('FA')
        break
    elif d[x1]:
        print('NFA')
        break
    d[x1]=True
    x = x1
