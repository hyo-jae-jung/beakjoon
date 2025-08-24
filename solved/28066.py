from sys import stdin  

N,K = map(int,stdin.readline().strip().split())
arr = list(range(1,N+1))

while N > 1 and N >= K:
    tmp_arr = []

    for i in range(N%K,0,-1):
        tmp_arr.append(arr[-i])

    for i in range(0,N-K+1,K):
        tmp_arr.append(arr[i])

    arr = tmp_arr
    N = len(arr)

print(arr[0])
