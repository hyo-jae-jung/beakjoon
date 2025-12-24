from sys import stdin  

n = int(stdin.readline().strip())
arr = list(map(int,stdin.readline().strip().split()))
s = int(stdin.readline().strip()) - 1

visited = [False]*n
visited[s] = True
ans = 1
stack = [s]

while stack:
    u = stack.pop()
    
    if (i:=u - arr[u]) >= 0 and not visited[i]:
        visited[i] = True
        stack.append(i)
        ans+=1

    if (j:=u + arr[u]) < n and not visited[j]:
        visited[j] = True
        stack.append(j)
        ans+=1
    
print(ans)
