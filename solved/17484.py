from sys import stdin   

N,M = map(int,stdin.readline().strip().split())
space = [list(map(int,stdin.readline().strip().split())) for _ in range(N)]

ans = N*M*100+1

stack = []
for col,val in enumerate(space[0]):
    stack.append((val,col,0,0))

while stack:
    val,col,row,state = stack.pop()

    if row+1 >= N:
        ans = min(ans,val)
        continue
    
    for i,j in enumerate(range(col-1,col+2),1):
        if j >= 0 and j < M and i != state and ans > val+space[row+1][j]:
            stack.append((val+space[row+1][j],j,row+1,i))
    
print(ans)
