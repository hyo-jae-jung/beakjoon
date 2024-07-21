from sys import stdin  

N,a,b = map(int,stdin.readline().strip().split())

arr = []
for _ in range(N):
    arr.append(list(map(int,stdin.readline().strip().split())))

ans = 'HAPPY'
for i in range(N):
    if arr[i][b-1] > arr[a-1][b-1]:
        ans = 'ANGRY'
        break

if ans == 'HAPPY':
    for i in range(N):
        if arr[a-1][i] > arr[a-1][b-1]:
            ans = 'ANGRY'
            break

print(ans)
