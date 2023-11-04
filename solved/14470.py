from sys import stdin 

A = int(stdin.readline().strip())
B = int(stdin.readline().strip())
C = int(stdin.readline().strip())
D = int(stdin.readline().strip())
E = int(stdin.readline().strip())

print(-A*C + D + B*E if A<=0 else (B-A)*E)
