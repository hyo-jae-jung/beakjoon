from sys import stdin   

N,K = map(int,stdin.readline().strip().split())

def f(n):
    if n == 0:
        return 1
    return (n)*(f(n-1))

print((f(N+K-1)//(f(K-1)*f(N)))%1_000_000_000)
