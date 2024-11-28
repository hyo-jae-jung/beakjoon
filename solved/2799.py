from sys import stdin  

M,N = map(int,stdin.readline().strip().split())
windows = []
for _ in range(M*5+1):
    windows.append(stdin.readline().strip())

ans = [0]*5

for j in range(1,M*5+1,5):
    for i in range(1,N*5+1,5):
        cnt = 0
        for k in range(4):
            if windows[j+k][i] == '*':
                cnt+=1
        
        ans[cnt]+=1

print(*ans)
