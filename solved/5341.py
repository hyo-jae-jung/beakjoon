from sys import stdin  

ans = []
while (tmp:=int(stdin.readline().strip())) != 0:
    ans.append(tmp*(tmp+1)//2)

print(*ans,sep='\n')
