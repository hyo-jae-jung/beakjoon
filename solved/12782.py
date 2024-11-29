from sys import stdin  

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    a,b = stdin.readline().strip().split()
    zero,one = 0,0
    for i,j in zip(a,b):
        if i != j:
            if i == '0':
                zero+=1
            else:
                one+=1
    ans.append(max(zero,one))

print(*ans,sep='\n')
