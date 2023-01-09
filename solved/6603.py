from sys import stdin 
from itertools import combinations as comb

Inp = []
while True:
    inp = list(map(int,stdin.readline().strip().split()))
    if inp[0] == 0:
        break
    Inp.append(inp[1:])

for i in Inp:
    for j in comb(i,6):
        print(*j)
    print('')
