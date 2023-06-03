from sys import stdin 

x1,y1 = map(int,stdin.readline().strip().split())
x2,y2 = map(int,stdin.readline().strip().split())
x3,y3 = map(int,stdin.readline().strip().split())

vx1,vy1 = x2-x1,y2-y1
vx2,vy2 = x3-x1,y3-y1

criteria = vx1*vy2 - vy1*vx2

if criteria > 0:
    print(1)
elif criteria < 0:
    print(-1)
else:
    print(0)
