from sys import stdin 

T = int(stdin.readline().strip())
answer = []
for _ in range(T):
    n = int(stdin.readline().strip())
    rooms = [0]*(n+1)
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j%i == 0:
                rooms[j]+=1
    answer.append(sum(1 if i%2 else 0 for i in rooms[1:]))

print(*answer,sep='\n')
