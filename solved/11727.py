import sys

n = int(sys.stdin.readline().strip())

a,b = 1,3
for _ in range(2,n):
    c = 2*a%10007 + b%10007
    a = b
    b = c

if n == 1:
    print(a)
else:
    print(b%10007)
