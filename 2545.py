from sys import stdin 
from heapq import heapify,heappop,heappush 

T = int(stdin.readline().strip())
answer = []
for _ in range(T):
    _ = stdin.readline()
    A,B,C,D = map(int,stdin.readline().strip().split())
    bread = [-A,-B,-C]
    heapify(bread)

    while D:
        
        if len(set(bread)) == 1:
            portion = D//3
            rest = D%3
            answer.append(((-bread[0] - portion)**(3-rest))*((-bread[0] - portion - 1)**rest))
            break

        first = -heappop(bread)
        second = -heappop(bread)
        diff = first + bread[0]
        if diff >= D:
            first-=D
            D = 0
        else:
            first-=diff
            D-=diff            
        heappush(bread,-first)
        heappush(bread,-second)
    else:
        answer.append(bread[0]*bread[1]*bread[2]*-1)

print(*answer,sep='\n')
