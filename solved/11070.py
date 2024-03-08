from sys import stdin 

T = int(stdin.readline().strip())

ans = []    
for _ in range(T):
    n,m = map(int,stdin.readline().strip().split())
    d = {}
    for i in range(1,n+1):
        d.update({i:{'score':0,'lose':0}})

    for _ in range(m):
        a,b,p,q = map(int,stdin.readline().strip().split())
        d[a]['score']+=p
        d[b]['score']+=q
        d[a]['lose']+=q
        d[b]['lose']+=p
        
    p_scores = []
    for i in d.values():
        if i['score'] == 0 and i['lose'] == 0:
            p_scores.append(0)
        else:
            p_scores.append(int(1000*(i['score']**2/(i['score']**2+i['lose']**2))))
    
    ans.append((max(p_scores),min(p_scores)))

for i in ans:
    print(*i,sep='\n')
    