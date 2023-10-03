from sys import stdin 

T = int(stdin.readline().strip())
answer = []
for _ in range(T):
    X = set(stdin.readline().strip())
    answer.append(len(X))

print(*answer,sep='\n')
