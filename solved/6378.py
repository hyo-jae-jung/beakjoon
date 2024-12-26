from sys import stdin  

ans = []
while (N:=stdin.readline().strip()) != '0':
    while len(N) > 1:
        tmp = 0
        for i in N:
            tmp+=int(i)
        N = str(tmp)
    else:
        ans.append(N)

print(*ans,sep='\n')
