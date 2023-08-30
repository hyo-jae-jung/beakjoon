from sys import stdin 

T = int(stdin.readline().strip())
answer = []
for _ in range(T):
    tmp = stdin.readline().strip()
    answer.append(tmp.count('0'))

print(*answer,sep='\n')
