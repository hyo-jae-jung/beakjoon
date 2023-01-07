from sys import stdin 

N,K = map(int,stdin.readline().strip().split())

arr = []

for i in range(N+1):
    temp = []
    for j in range(N+1):
        if i == j or j == 0:
            temp.append(1)
        else:
            temp.append(None)
    arr.append(temp)

def binomial_coefficient(n,k):

    if isinstance(arr[n][k],int):
        return arr[n][k]
    
    for i in range(2,N+1):
        for j in range(1,i):
            arr[i][j] = arr[i-1][j] + arr[i-1][j-1]

    return arr[n][k]

print(binomial_coefficient(N,K)%10007)

