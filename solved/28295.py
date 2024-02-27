from sys import stdin 
degree = 0
for _ in range(10):
    t = int(stdin.readline().strip())
    if t == 1:
        degree+=90
    elif t == 2:
        degree+=180
    else:
        degree-=90

ans = degree%360
if ans == 0:
    print('N')
elif ans == 90:
    print('E')
elif ans == 180:
    print('S')
else:
    print('W')
    