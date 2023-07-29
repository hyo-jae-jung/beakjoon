from sys import stdin 

T = int(stdin.readline().strip())
answer = []
for _ in range(T):
    V,E = map(int,stdin.readline().strip().split())
    answer.append(2+E-V)

print(*answer,sep='\n')
