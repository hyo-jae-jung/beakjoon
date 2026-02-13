from sys import stdin  
from copy import deepcopy

N = int(stdin.readline().strip())
arr = [list(map(int,stdin.readline().strip().split())) for _ in range(N)]

def solution(arr,n,i=0):
    arr_copy = deepcopy(arr)
    arr_copy[1][(i+1)%3]+=arr_copy[0][i]
    arr_copy[1][(i+2)%3]+=arr_copy[0][i]
    if n == 2:
        return min(arr_copy[1][(i+1)%3],arr_copy[1][(i+2)%3])

    arr_copy[2][i]+=min(arr_copy[1][(i+1)%3],arr_copy[1][(i+2)%3])
    arr_copy[2][(i+1)%3]+=arr_copy[1][(i+2)%3]
    arr_copy[2][(i+2)%3]+=arr_copy[1][(i+1)%3]

    if n == 3:
        return min(arr_copy[2][(i+1)%3],arr_copy[2][(i+2)%3])

    for j in range(3,n):
        for k in range(3):
            arr_copy[j][k]+=min(arr_copy[j-1][(k+1)%3],arr_copy[j-1][(k+2)%3])
    
    return min((arr_copy[n-1][l] for l in range(3) if l != i))

print(min(solution(arr,N,0),solution(arr,N,1),solution(arr,N,2)))
