from sys import stdin

N = int(stdin.readline().strip())

def f(x):
    if x < 2:
        return 0
    else:
        return x-2

print(8*2**(N-1)+1+f(N)*2)
