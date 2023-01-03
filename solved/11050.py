from sys import stdin
from math import factorial as f

N,K = map(int,stdin.readline().strip().split())

print(int(f(N)/(f(K)*f(N-K))))
