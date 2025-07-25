from sys import stdin   

M,N = map(int,stdin.readline().strip().split())
graph = {}
for _ in range(M):
    a,b = stdin.readline().strip().split()
    if not graph.get(a):
        graph.update({a:[]})
    graph[a].append(b)

ans = []

def is_translated(s1,s2):
    global graph
    stack = [s1]
    visited = set()

    while stack:
        s = stack.pop()
        if s == s2:
            return True
        if s in visited:
            continue
        visited.add(s)
        if graph.get(s):
            for i in graph.get(s):
                if i not in visited:
                    stack.append(i)    
    return False

for _ in range(N):
    word1,word2 = stdin.readline().strip().split()
    if len(word1) == len(word2):
        for i,j in zip(word1,word2):
            if not is_translated(i,j):
                ans.append('no')
                break
        else:
            ans.append('yes')
    else:
        ans.append('no')

print(*ans,sep='\n')
