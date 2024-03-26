from sys import stdin 
from collections import defaultdict 


R = int(stdin.readline().strip())
sanggun_by_round = stdin.readline().strip()

friends = []
N = int(stdin.readline().strip())
for _ in range(N):
    friends.append(stdin.readline().strip())

rounds = []
for i in range(R):
    tmp = ''
    for j in range(N):
        tmp+=friends[j][i]
    rounds.append(tmp)

def machine(x):
    if x=='S':
        return (2,1,0)
    if x=='P':
        return (1,0,2)
    if x=='R':
        return (0,2,1)

def fair(sangun,round):
    m = machine(sangun)
    d = defaultdict(int)
    for i in round:
        d[i]+=1
    return d['P']*m[0]+d['S']*m[1]+d['R']*m[2]

def cheat(round):
    d = defaultdict(int)
    for i in round:
        d[i]+=1
    return max(d['P']*2+d['S']*1+d['R']*0,d['P']*1+d['S']*0+d['R']*2,d['P']*0+d['S']*2+d['R']*1)

ans1 = 0
ans2 = 0
for i,j in zip(sanggun_by_round,rounds):
    ans1+=fair(i,j)
    ans2+=cheat(j)

print(ans1,ans2,sep='\n')
