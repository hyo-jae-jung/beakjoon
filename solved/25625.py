from sys import stdin 

x,y = map(int,stdin.readline().strip().split())
print(y%x + (0 if (y//x) == 1 else x))
