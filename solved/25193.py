from sys import stdin 
import math

N = int(stdin.readline().strip())
S = list(stdin.readline().strip())
another = 0
for _ in range(N):
    tmp = S.pop()
    if tmp != 'C':
        another+=1

print(math.ceil((N-another)/(another+1)))
