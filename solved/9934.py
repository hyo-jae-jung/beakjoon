from sys import stdin 

K = int(stdin.readline().strip())
arr =list(map(int,stdin.readline().strip().split()))

lev = [[] for _ in range(K)]

def dfs(arr,k=0):
    i = len(arr)//2
    lev[k].append(arr[i])

    if k == K-1:
        return True

    dfs(arr[:i],k+1)
    dfs(arr[i+1:],k+1)

dfs(arr)

for i in lev:
    print(*i)
