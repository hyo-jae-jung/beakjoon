from sys import stdin 

n = int(stdin.readline().strip())

def fibonacci(n):
    a,b = 1,1
    for _ in range(2,n+1):
        tmp = b
        b = (1 + a + b)%((10**9)+7)
        a = tmp
    return b

print(fibonacci(n))
