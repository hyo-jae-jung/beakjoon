from sys import stdin 

n = int(stdin.readline().strip())

def fibonacci(n):
    a,b = 1,1
    for _ in range(3,n+1):
        tmp = b
        b = (a+b)%(10**9+7)
        a = tmp
    return b

print(fibonacci(n),(n-2)%(10**9+7))
