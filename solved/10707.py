from sys import stdin 

a = int(stdin.readline().strip())
b = int(stdin.readline().strip())
c = int(stdin.readline().strip())
d = int(stdin.readline().strip())
e = int(stdin.readline().strip())

print(min(a*e,b+d*(e-c if e>c else 0)))
