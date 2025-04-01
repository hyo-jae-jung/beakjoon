from sys import stdin  

a,b = map(int,stdin.readline().strip().split())

def col(n):
    return n//4 + (1 if n%4 > 0 else 0)

def row(n):
    return n%4 if n%4 > 0 else 4

print(abs(col(a)-col(b)) + abs(row(a) - row(b)))
