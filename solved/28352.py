from sys import stdin  

N = int(stdin.readline().strip())

ans = 3628800
for i in range(11,N+1):
    ans*=i

print((ans//3628800)*6)
