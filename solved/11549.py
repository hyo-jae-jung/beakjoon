from sys import stdin  

T = stdin.readline().strip()
ABCDE = stdin.readline().strip().split()

print(len([i for i in ABCDE if i == T]))
