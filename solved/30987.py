from sys import stdin 

x1,x2 = map(int,stdin.readline().strip().split())
a,b,c,d,e = map(int,stdin.readline().strip().split())

print(int(a*(x2**3-x1**3)/3+(b-d)*(x2**2-x1**2)/2+(c-e)*(x2-x1)))

