from sys import stdin  

T = int(stdin.readline().strip())
N = int(stdin.readline().strip())
F = map(int,stdin.readline().strip().split())
if T <= sum(F):
    print("Padaeng_i Happy")
else:
    print("Padaeng_i Cry")
    