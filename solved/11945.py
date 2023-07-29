from sys import stdin 

N,M = map(int,stdin.readline().strip().split())

answer = []
for _ in range(N):
    answer.append(''.join(list(reversed(stdin.readline().strip()))))

print(*answer,sep='\n')
