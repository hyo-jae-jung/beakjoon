from sys import stdin  

A,B,C,X,Y = map(int,stdin.readline().strip().split())

a = A*X+B*Y
b = min(X,Y)*C*2 + (A*(X-min(X,Y)) if X > Y else B*(Y-min(X,Y)))
c = min(X,Y)*C*2 + 2*C*abs(X-Y)

print(min(a,b,c))
