import sys

space = []
while True:
    a,b = map(int,sys.stdin.readline().strip().split())
    if a == 0 and b == 0:
        break
    else:
        space.append((a,b))

for i,j in space:
    if j%i == 0:
        print('factor')
    elif i%j == 0:
        print('multiple')
    else:
        print('neither')
