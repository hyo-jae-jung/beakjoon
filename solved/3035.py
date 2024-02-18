from sys import stdin 

R,C,ZR,ZC = map(int,stdin.readline().strip().split())
article = []
for _ in range(R):
    article.append(stdin.readline().strip())
ans = []
for i in article:
    tmp = ''
    for j in i:
        tmp+=j*ZC

    for _ in range(ZR):
        ans.append(tmp)

print(*ans,sep='\n')
