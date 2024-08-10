from sys import stdin  

a = int(stdin.readline().strip())
x = int(stdin.readline().strip())
b = int(stdin.readline().strip())
y = int(stdin.readline().strip())
T = int(stdin.readline().strip())

print((T-30 if T > 30 else 0)*21*x + a,(T-45 if T > 45 else 0)*21*y + b)
