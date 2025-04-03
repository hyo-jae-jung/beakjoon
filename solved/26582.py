from sys import stdin  

n = int(stdin.readline().strip())
ans = []

def solution(V=0,W=0,I=0):

    global i
    if I == i:
        return True

    global w,vw
    if W+treasures[I][1] <= w and vw[W+treasures[I][1]] < V+treasures[I][0]:
        vw[W+treasures[I][1]] = V+treasures[I][0]
        solution(V=V+treasures[I][0],W=W+treasures[I][1],I=I+1)

    solution(V,W,I=I+1)

for _ in range(n):
    i,w = map(int,stdin.readline().strip().split())
    treasures = []
    vw = [0]*(w+1)
    for _ in range(i):
        val,weight = map(int,stdin.readline().strip().split())
        treasures.append((val,weight))
        
    solution()
    ans.append(max(vw))

print(*ans,sep='\n')
