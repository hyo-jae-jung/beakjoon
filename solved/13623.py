from sys import stdin  

A,B,C = stdin.readline().strip().split()

if A == B == C:
    print("*")
elif A == B:
    print("C")
elif A == C:
    print("B")
elif B == C:
    print("A")
