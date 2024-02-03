from sys import stdin 

N = int(stdin.readline().strip())
A,B = 0,0
for _ in range(N):
    ai,bi = map(int,stdin.readline().strip().split())
    if ai > bi:
        A+=1
    elif ai < bi:
        B+=1

print(A,B)
