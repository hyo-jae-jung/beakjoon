from sys import stdin  

ans = []
while (t:=int(stdin.readline().strip()))!=0:
    square_cnt = 0
    for i in range(t+1):
        square_cnt+=i**2
    
    ans.append(square_cnt)

print(*ans,sep='\n')
