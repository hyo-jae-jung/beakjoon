from sys import stdin  

N,M = map(int,stdin.readline().strip().split())
room = []
for _ in range(N):
    room.append(list(map(int,stdin.readline().strip().split())))

def solution(n):

    for i in range(M-n):
        if room[n-1][i] == 1:
            return 1
        
    for j in range(N-n+1):
        if room[n+j-1][M-n] == 1:
            return 1

    return 0

ans = 0
for i in range(1,min(M,N)+1):
    ans+=solution(i)

print(ans)

