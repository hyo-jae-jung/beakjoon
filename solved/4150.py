from sys import stdin 

N = int(stdin.readline().strip())

def fibonacci(n):
    a,b = 1,1
    for _ in range(3,n+1):
        tmp=b
        b+=a
        a=tmp
    return b

print(fibonacci(N))
