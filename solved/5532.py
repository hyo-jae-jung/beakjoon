from sys import stdin 
from math import ceil

L = int(stdin.readline().strip())
A = int(stdin.readline().strip())
B = int(stdin.readline().strip())
C = int(stdin.readline().strip())
D = int(stdin.readline().strip())

print(L-max(ceil(A/C),ceil(B/D)))
