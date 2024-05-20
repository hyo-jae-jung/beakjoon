from sys import stdin  

ans = []
while (t:=stdin.readline().strip()) != '':
    N,B,M = map(float,t.split( ' '))
    y = 0
    while N*(1+B/100)**y < M:
        y+=1
    ans.append(y)

print(*ans,sep='\n')
