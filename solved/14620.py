from sys import stdin   

N = int(stdin.readline().strip())
flower_garden = [list(map(int,stdin.readline().strip().split())) for _ in range(N)]

ans = float('inf')
visited = [[False]*N for _ in range(N)]

def check(arr,x,y):
    if arr[y][x] == True:
        return False
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        if arr[y+dy][x+dx] == True:
            return False
    return True

def blossom(arr,x,y,t=True):
    arr[y][x] = t
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        arr[y+dy][x+dx] = t

def rent_cost(arr,x,y):
    result = 0
    result+=arr[y][x]
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        result+=arr[y+dy][x+dx]
    return result

def solution(seed_cnt=0,val=0):
    global N,flower_garden,ans,visited
    if seed_cnt == 3:
        ans = min(ans,val)
        return 
    
    for i in range(1,N-1):
        for j in range(1,N-1):
            if check(visited,j,i):
                blossom(visited,j,i,True)
                solution(seed_cnt+1,val+rent_cost(flower_garden,j,i))
                blossom(visited,j,i,False)

solution()
print(ans)
