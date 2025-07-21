from sys import stdin  

T = [int(stdin.readline().strip()) for _ in range(4)]

if 1800 - sum(T,300) >= 0:
    print('Yes')
else:
    print("No")

