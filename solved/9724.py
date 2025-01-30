from sys import stdin   
from bisect import bisect_left

T = int(stdin.readline().strip())
arr = []
i = 1
while i**3 <= 2_000_000_000:
    arr.append(i**3)
    i+=1

ans = []
for i in range(1,T+1):
    A,B = map(int,stdin.readline().strip().split())
    ans.append(f"Case #{i}: {bisect_left(arr,B) - bisect_left(arr,A)}")

print(*ans,sep='\n')
