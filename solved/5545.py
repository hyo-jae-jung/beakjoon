from sys import stdin 

N = int(stdin.readline().strip())
A,B = map(int,stdin.readline().strip().split())
C = int(stdin.readline().strip())
D = []
for _ in range(N):
    D.append(int(stdin.readline().strip()))

D.sort()

while D:
    temp = D.pop()
    if temp > ((A+B)/A-1)*C:
        C+=temp
        A+=B
    else:
        break

print(C//A)
