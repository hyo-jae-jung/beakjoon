from sys import stdin 

N = int(stdin.readline().strip())

if N%3 == 0:
    if (N//3)%2 == 0:
        print('CY')
    else:
        print('SK')
else:
    if (N//3)%2 != 0:
        print('CY')
    else:
        print('SK')
