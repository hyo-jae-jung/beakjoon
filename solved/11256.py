from sys import stdin 

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    J,N = map(int,stdin.readline().strip().split())
    boxes = []
    for _ in range(N):
        a,b = map(int,stdin.readline().strip().split())
        boxes.append(a*b)
    
    boxes.sort()

    cnt = 0
    while J > 0:
        space = boxes.pop()
        J-=space
        cnt+=1
    ans.append(cnt)

print(*ans,sep='\n')    
