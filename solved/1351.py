from sys import stdin 
from collections import defaultdict

N,P,Q = map(int,stdin.readline().strip().split())

A = defaultdict(int)
A[0] = 1

def recursion(n):

    if not A[n]:
        A[n] = recursion(n//P) + recursion(n//Q)

    if n == 0:
        return 1
    
    return A[n]

print(recursion(N))
