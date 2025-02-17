from sys import stdin  

N = int(stdin.readline().strip())

ans = []
for i in list(range(1,2*N)) + list(range((4*N-3)//2,0,-1)):
    tmp = ''
    for j in list(range(1,2*N)) + list(range((4*N-3)//2,0,-1)):
        print(i,j)
        if i == 1:
            tmp+="*"
            
        if i == 2:
            if j == 1:
                tmp+="*"
            else:
                tmp+=" "
        if i == 3:
            if j == 2:
                tmp+=" "
            else:
                tmp+="*"

    ans.append(tmp)

print(*ans,sep='\n')
