from sys import stdin  

N,M,R = map(int,stdin.readline().strip().split())
arr = [list(map(int,stdin.readline().strip().split())) for _ in range(N)]

def rotate(arr):
    d = min(N,M)//2
    for j in range(d):
        for i in range(1,M-j*2):
            arr[j][i-1+j],arr[j][i+j] = arr[j][i+j],arr[j][i-1+j]

        for i in range(1,N-j*2):
            arr[i-1+j][M-1-j],arr[i+j][M-1-j] = arr[i+j][M-1-j],arr[i-1+j][M-1-j]

        for i in range(M-1-j*2,0,-1):
            arr[N-1-j][i+j],arr[N-1-j][i-1+j] = arr[N-1-j][i-1+j],arr[N-1-j][i+j]

        for i in range(N-1-j*2,1,-1):
            arr[i+j][j],arr[i-1+j][j] = arr[i-1+j][j],arr[i+j][j]

for _ in range(R):
    rotate(arr)

for i in arr:
    print(*i)
