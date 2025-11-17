from sys import stdin    

N = int(stdin.readline().strip())
arr = [1] + [0]*2000
for _ in range(N):
    tmp = [0]*2001
    for i in [50,10,5,1]:
        for j in range(2000,i-1,-1):
            tmp[j] = max(tmp[j],arr[j-i])
    arr = tmp.copy()

print(arr.count(1))
