import sys
from math import abs

T = int(sys.stdin.readline().strip())

data_list = []

for i in range(T):
    x1,y1,r1,x2,y2,r2 = map(int,sys.stdin.readline().split())
    data_list.append([x1,y1,r1,x2,y2,r2])

for i in data_list:
    if (((x1-x2)**2 + (y1-y2)**2)**0.5 > r1+r2) or (((x1-x2)**2 + (y1-y2)**2)**0.5 <abs(r1-r2)):
        print(0)
    elif (((x1-x2)**2 + (y1-y2)**2)**0.5 == r1+r2) or (((x1-x2)**2 + (y1-y2)**2)**0.5 == abs(r1-r2)):
        print(1)
    elif 
