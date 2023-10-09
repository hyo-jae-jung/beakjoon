from sys import stdin 

N = int(stdin.readline().strip()) 

answer = [[True]*3 for _ in range(N)]
arr = []
for _ in range(N):
    arr.append(list(map(int,stdin.readline().strip().split())))

for i in range(3):
    for j in range(N):
        for k in range(j+1,N):
            if arr[j][i] == arr[k][i]:
                answer[j][i],answer[k][i] = False,False

for i,j in zip(arr,answer):
    print(sum(k for k,l in zip(i,j) if l))
