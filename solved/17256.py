from sys import stdin  

ax,ay,az = map(int,stdin.readline().strip().split())
cx,cy,cz = map(int,stdin.readline().strip().split())
print(cx-az,cy//ay,cz-ax)
