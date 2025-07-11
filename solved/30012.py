def solution(E):
    global S,K,L
    distance = abs(S-E)
    if (a:=distance - 2*K) < 0:
        return -a
    if a == 0:
        return 0
    return a*L

from sys import stdin  
S,N = map(int,stdin.readline().strip().split())
E = list(map(int,stdin.readline().strip().split()))
K,L = map(int,stdin.readline().strip().split())

min_consume_strength = 10**10+1
min_consume_idx = 10**5+1

for i in range(N):
    if (s:=solution(E[i])) < min_consume_strength:
        min_consume_strength = s
        min_consume_idx = i + 1

print(min_consume_strength,min_consume_idx)
