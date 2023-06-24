from sys import stdin 

n = int(stdin.readline().strip())
answer = []
for _ in range(n):
    answer.append('='*int(stdin.readline().strip()))
print(*answer,sep='\n')
