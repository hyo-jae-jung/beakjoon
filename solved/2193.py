from sys import stdin 

N = int(stdin.readline().strip())

def fibonacci(n):
    a,b = 1,1
    for _ in range(n-2):
        tmp = b
        b = a + b
        a = tmp
    return b

print(fibonacci(N))
