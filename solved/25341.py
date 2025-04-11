from sys import stdin   

N,M,Q = map(int,stdin.readline().strip().split())
Ms = []
for _ in range(M):
    Ms.append(list(map(int,stdin.readline().strip().split())))

O = list(map(int,stdin.readline().strip().split()))

Is = []
for _ in range(Q):
    Is.append(list(map(int,stdin.readline().strip().split())))

d = {}
for i in range(N):
    d.update({i+1:0})

for i in range(M):
    for j in range(Ms[i][0]):
        d[Ms[i][j+1]]+=Ms[i][j+1+Ms[i][0]]*O[i]
    Ms[i][-1]*=O[i]

def solution(l,m,ms):
    ans = O[-1]
    for i in range(m):
        ans+=ms[i][-1]
    ans+=sum(map(lambda x,y:x*y,l,d.values()))
    return ans

for i in Is:
    print(solution(i,M,Ms))
