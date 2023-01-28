from sys import stdin 

N = int(stdin.readline().strip())
answer = []
for i in range(1,N+1):
    answer.append(f'{i}. {input()}')

print(*answer, sep='\n')

