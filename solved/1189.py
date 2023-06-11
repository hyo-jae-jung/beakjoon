from sys import stdin
from collections import deque

R,C,K = map(int,stdin.readline().strip().split())
chart = deque()
for _ in range(R):
    chart.appendleft(list(stdin.readline().strip()))

chart = list(chart)

def dfs(x=0,y=0,s=set()):
    if x < 0 or y < 0 or x >= C or y >= R:
        return False

    if (x,y) in s:
        return False

    if x == C-1 and y == R-1 and len(s) == K-1:
        global answer
        answer+=1
        return True

    if chart[y][x] == '.':
        dfs(x-1,y,s|set([(x,y)]))
        dfs(x+1,y,s|set([(x,y)]))
        dfs(x,y-1,s|set([(x,y)]))
        dfs(x,y+1,s|set([(x,y)]))
        return True

answer = 0
dfs()

print(answer)
