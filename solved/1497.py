from sys import stdin  

N,M = map(int,stdin.readline().strip().split())

guitars = []
for _ in range(N):
    _,songs = stdin.readline().strip().split()
    available = 0
    for i in range(M):
        if songs[i] == 'Y':
            available+= 1 << i

    guitars.append(available)

visited = [False]*N

arr = [float('inf')]*(M+1)

def solution(idx=0,guitar_cnt=0,val=0):
    global N,guitars,visited

    e = 0
    tmp_cnt = 0
    while val >= 2**e:
        if val & 2**e == 2**e:
            tmp_cnt+=1
        e+=1
    arr[tmp_cnt] = min(arr[tmp_cnt],guitar_cnt)

    for i in range(idx,N):
        if not visited[i]:
            visited[i] = True
            solution(i+1,guitar_cnt+1,val|guitars[i])
            visited[i] = False

solution()
for i in range(M,0,-1):
    if arr[i] != float('inf'):
        print(arr[i])
        break
else:
    print(-1)
