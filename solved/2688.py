arr = [[0]*10 for _ in range(65)]
for i in range(10):
    arr[1][i] = 1

for i in range(1,64):
    for j in range(10):
       for k in range(j,10):
          arr[i+1][k]+=arr[i][j]

from sys import stdin  

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    ans.append(sum(arr[int(stdin.readline().strip())]))

print(*ans,sep='\n')
