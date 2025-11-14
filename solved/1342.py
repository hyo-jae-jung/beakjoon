from sys import stdin   

items = list(stdin.readline().strip())
ans = 0
S = set()
visited = [False]*len(items)

def solution(val=''):
    global items,ans,S,visited 
    if len(val) == len(items) and val not in S:
        ans+=1
        S.add(val)
        return 
    
    for i,item in enumerate(items):
        if not visited[i]:
            visited[i] = True
            if not val or val[-1] != item:
                solution(val+item)
            visited[i] = False

solution()
print(ans)
