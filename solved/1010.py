from sys import stdin
from math import factorial as f
T = int(stdin.readline().strip())
answer = []
for _ in range(T):
    N,M = map(int,stdin.readline().strip().split())
    answer.append(f(M)/(f(N)*f(M-N)))

for i in answer:
    print(f'{i:.0f}')
