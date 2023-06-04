from sys import stdin 

N = int(stdin.readline().strip())
graph = [[] for _ in range(N+1)]
answer = set()
visited = [False]+[True]*(N)
for a in range(1,N+1):
    b = int(stdin.readline().strip())
    if a == b:
        answer.add(a)
        visited[a] = False
    else:
        graph[a].append(b)

print(answer,graph,visited)

def dfs(start):
    stack = [start]
    s = set(stack)
    while stack:
        p = stack.pop()
        if visited[p]:
            visited[p] = False
            s.add(*graph[p])
            if [start] == graph[p]:
                return s
            stack.extend(graph[p])
    else:
        return set()
    
"""
중간에라도 순환이 있으면 체크해야함.. 다시 짜야됨
"""

print(dfs(4))

# i=1
# while any(visited):
#     if visited[i]:
#         answer = answer | dfs(i)
#         print(visited,answer)
#     i+=1
# else:
#     print(answer)
