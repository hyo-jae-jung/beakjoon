from sys import stdin 
from itertools import combinations as comb

N = int(stdin.readline().strip())

arr = []
for _ in range(N):
    arr.append(list(map(int,stdin.readline().strip().split())))

ans = float('inf')
for i in range(1,N+1):
    for j in comb(arr,i):
        tmp = [1,0]
        for sour,bitter in j:
            tmp = [tmp[0]*sour,tmp[1]+bitter]
        
        ans = min(ans,abs(tmp[0] - tmp[1]))

print(ans)

