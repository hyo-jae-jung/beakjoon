from sys import stdin 

T = int(stdin.readline().strip())
answer = []

for _ in range(T):
    d = []
    N = int(stdin.readline().strip())
    for _ in range(N):
        S,L = stdin.readline().strip().split()
        d.append((S,int(L)))
    else:
        d.sort(key=lambda x:x[1])
        answer.append(d[-1][0])

print(*answer,sep='\n')    
