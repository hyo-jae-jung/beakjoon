from sys import stdin 

K = int(stdin.readline().strip())

def fibonacci(n):
    a,b = 1,0
    for _ in range(n):
        tmp = b
        b = b + a
        a = tmp
    return (a,b)

print(*fibonacci(K))
