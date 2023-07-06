from sys import stdin 

T = int(stdin.readline().strip())
answer = []
for _ in range(T):
    n = int(stdin.readline().strip())
    graph = []
    for _ in range(2):
        graph.append(list(map(int,stdin.readline().strip().split())))
    
