from sys import stdin 

K = int(stdin.readline().strip())
D1,D2 = map(int,stdin.readline().strip().split())
print((4*(K**2) - (D1-D2)**2)/4)
