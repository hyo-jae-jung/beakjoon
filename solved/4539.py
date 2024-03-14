from sys import stdin 

n = int(stdin.readline().strip())
ans = []
for _ in range(n):
    x = list(map(int,stdin.readline().strip()))
    for i,j in enumerate(range(len(x)-1,0,-1),1):
        if x[j] >= 5:
            x[j-1]+=1
        x[j] = 0
    ans.append(''.join(map(str,x)))

print(*ans,sep='\n')
