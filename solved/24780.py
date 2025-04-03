from sys import stdin  

K = int(stdin.readline().strip())
graph = {}
while (i:=stdin.readline().strip()) != '-1':
    l = list(map(int,i.split()))
    for j in l[1:]:
        if graph.get(j):
            graph[j].append(l[0])
        else:
            graph.update({j:[l[0]]})


ans = []
def dfs(n):
    global ans, graph
    ans.append(n)

    if graph.get(n):
        for i in graph.get(n):
            dfs(i)

dfs(K)
print(*ans)
