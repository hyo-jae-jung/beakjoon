from sys import stdin 

N = int(stdin.readline().strip())
ans = []
for _ in range(N):
    tmp = []
    x,y = stdin.readline().strip().split()
    for i,j in zip(x,y):
        tmp.append(ord(j) - ord(i) + (26 if ord(j) - ord(i) < 0 else 0))
    ans.append("Distances: "+' '.join(map(str,tmp)))

print(*ans,sep='\n')
