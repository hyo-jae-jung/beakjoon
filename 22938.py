from sys import stdin 

x1,y1,r1 = map(int,stdin.readline().strip().split())
x2,y2,r2 = map(int,stdin.readline().strip().split())

print('YES' if ((x1-x2)**2+(y1-y2)**2)**0.5 <= r1+r2 else 'NO')

