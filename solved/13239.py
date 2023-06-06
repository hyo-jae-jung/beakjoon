from sys import stdin 

t = int(stdin.readline().strip())
arr = [[0]*1001 for _ in range(1001)]

def pascals_rule(n,k):
    if arr[n][k]:
        return arr[n][k]

    if k == 0:
        arr[n][k] = n
        return 1

    if k == n:
        arr[n][k] = 1
        return 1
    
    arr[n-1][k-1] = pascals_rule(n-1,k-1)
    arr[n-1][k] = pascals_rule(n-1,k)
    return arr[n-1][k-1] + arr[n-1][k]

answer = []
for _ in range(t):
    n,k = map(int,stdin.readline().strip().split())
    answer.append(pascals_rule(n,k)%(10**9+7))

print(*answer,sep='\n')
