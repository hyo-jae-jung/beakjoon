from sys import stdin 
from collections import defaultdict

T = int(stdin.readline().strip())
answer = []
for _ in range(T):
    N = int(stdin.readline().strip())
    graph = defaultdict(int)
    for _ in range(N-1):
        A,B = map(int,stdin.readline().strip().split())
        graph[B] = A
    node1,node2 = map(int,stdin.readline().strip().split())
    