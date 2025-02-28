from sys import stdin   

N = int(stdin.readline().strip())
arr = []
for _ in range(N):
    arr.append(tuple(map(int,stdin.readline().strip().split())))

ans = []

arr.sort(key=lambda x:(-x[0],x[1]))

ans.append(arr[0]+arr[1])

arr.sort(key=lambda x:(x[1],-x[0]))

ans.append(arr[0]+arr[1])

for i in ans:
    print(*i)
    