N,M = map(int,input().split())

arr1 = []
arr2 = []

for _ in range(N):
    arr1.append(list(map(int,input().split())))

for _ in range(N):
    arr2.append(list(map(int,input().split())))

for i,j in zip(arr1,arr2):
    temp = []
    for k,l in zip(i,j):
        temp.append(str(k+l))
    print(' '.join(temp))
