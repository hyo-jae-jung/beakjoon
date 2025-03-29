from sys import stdin  

x,y = map(int,stdin.readline().strip().split())

def gcd(a,b):
    a,b = max(a,b),min(a,b)
    if a%b == 0:
        return b
    return gcd(b,a%b)

gcd_xy = gcd(x,y)

print((min(x,y)//gcd_xy-1)*gcd_xy+max(x,y))
