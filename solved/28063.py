from sys import stdin 

N = int(stdin.readline().strip())
x,y = map(int,stdin.readline().strip().split())

if N == 1:
    print(0)
elif N == 2:
    print(2)
elif N >= 3:
    if x in [1,N] and y in [1,N]:
        print(2)
    elif x in [1,N] or y in [1,N]:
        print(3)
    else:
        print(4)
    