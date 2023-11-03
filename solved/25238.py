from sys import stdin 

a,b = map(int,stdin.readline().strip().split())
print(0 if a*(100-b)/100 >= 100 else 1)
