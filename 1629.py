from sys import stdin 

A,B,C = map(int,stdin.readline().strip().split())
answer = 1
for _ in range(B):
    answer*=A%C
    answer%=C

print(answer)
