from sys import stdin  

t = int(stdin.readline().strip())
ans = []
for _ in range(t):
    a,b,c = map(int,stdin.readline().strip().split())
    tmp = (9000 - (a*15 + b*20 + c*25))
    A = tmp//40
    B = tmp%40
    minimum_score = A+(1 if B > 0 else 0)
    if minimum_score > 100:
        ans.append("impossible")
    else:
        ans.append(minimum_score)
    
print(*ans,sep='\n')
