from sys import stdin 

N = int(stdin.readline().strip())
answer = []

answer.append(sum(range(1,N+1)))
answer.append(sum(range(1,N+1))**2)
answer.append(sum(i**3 for i in range(1,N+1)))

print(*answer,sep='\n')
