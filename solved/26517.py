from sys import stdin 

k = int(stdin.readline().strip())
a,b,c,d = map(int,stdin.readline().strip().split())
print(*('Yes',a*k+b) if a*k+b == c*k+d else ('No',))
