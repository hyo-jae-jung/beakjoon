from sys import stdin   

N,M = map(int,stdin.readline().strip().split())
graph = {}
total = set()
for i in range(N):
    total.add(chr(65+i))

supply = total.copy()
for _ in range(M):
    start,end = stdin.readline().strip().split()
    if start != end:
        supply.discard(end)
        if graph.get(start):
            graph[start].append(end)
        else:
            graph.update({start:[end]})

arrest_status = stdin.readline().strip().split()

if arrest_status[0] == '0':
    print(N - len(supply))
else:
    if len(supply) == 0:
        print(0)
    else:
        arrest_nodes = set(arrest_status[1:])
        
        ans = set()
        def dfs(x,graph,arrest=set()):
            if x in arrest:
                return False
            ans.add(x)
            if graph.get(x):
                for node in graph[x]:
                    if node not in arrest:
                        dfs(node,graph,arrest_nodes)

        for i in supply:
            dfs(i,graph,arrest_nodes)

        print(len(ans - supply))
