from sys import stdin 

N,M = map(int,stdin.readline().strip().split())
chart = []
for _ in range(N):
    chart.append(list(map(int,stdin.readline().strip().split())))

def dfs(x,y):
    if x < 0 or y < 0 or x >= M or y >= N:
        return False
    
print(max(sum(chart,[])))
