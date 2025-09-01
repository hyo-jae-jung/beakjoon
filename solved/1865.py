from sys import stdin   

TC = int(stdin.readline().strip())
ans = []
for _ in range(TC):
    N,M,W = map(int,stdin.readline().strip().split())
    edges = []
    for _ in range(M):
        S,E,T = map(int,stdin.readline().strip().split())
        edges.append((S,E,T))
        edges.append((E,S,T))

    for _ in range(W):
        S,E,T = map(int,stdin.readline().strip().split())
        edges.append((S,E,-T))

    dist = [0]*(N+1)

    for _ in range(N-1):
        for s,e,t in edges:
            if dist[e] > dist[s] + t:
                dist[e] = dist[s] + t

    dist_ans = dist.copy()

    for s,e,t in edges:
        if dist[e] > dist[s] + t:
            dist[e] = dist[s] + t

    cycle = False
    for i in range(1,N+1):
        if dist[i] != dist_ans[i]:
            cycle = True
            break
    
    ans.append('YES' if cycle else 'NO')

print(*ans,sep='\n')
