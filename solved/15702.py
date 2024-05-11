from sys import stdin 

N,M = map(int,stdin.readline().strip().split())
scores = list(map(int,stdin.readline().strip().split()))
arr = []
for _ in range(M):
    a = stdin.readline().strip().split()
    total_score = 0
    for i,j in zip(scores,a[1:]):
        if j =='O':
            total_score+=i
    arr.append((int(a[0]),total_score))

arr.sort(key=lambda x:(-x[1],x[0]))
print(*arr[0])
