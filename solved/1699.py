from sys import stdin 
from collections import deque

N = int(stdin.readline().strip())

def bfs(n):

    nn = n
    cnt = 0
    while nn > 0:
        nn = nn - (int(nn**0.5))**2
        cnt+=1

    memo = [cnt]*100001

    q = deque([(n,0)])

    while q:

        n,c = q.popleft()

        if n == 0:
            cnt = min(cnt,c)

        for i in range(int(n**0.5),0,-1):
            if c < cnt and memo[n-i**2] > c+1:
                q.append((n-i**2,c+1))
                memo[n-i**2] = c+1
        
    return cnt

print(bfs(N))
