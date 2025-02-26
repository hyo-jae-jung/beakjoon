from sys import stdin  

a,b = map(int,stdin.readline().strip().split())

for i in range(1,min(a,b)+1):
    if a%i == 0 and b%i == 0:
        print(i,a//i,b//i)

