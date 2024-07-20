from sys import stdin  

ans = []
while (N:=int(stdin.readline().strip())) != 0:
    while N > 9:
        N = sum(map(int,list(str(N))))
    else:
        ans.append(N)

print(*ans,sep='\n')
