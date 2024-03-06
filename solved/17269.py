from sys import stdin 
from collections import defaultdict 

N,M = map(int,stdin.readline().strip().split())
A,B = stdin.readline().strip().split()

d = defaultdict(int)
for i,j in zip(range(26),[3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]):
    d[chr(i+65)]=j

mixed = ''
i = 0
while i < max(N,M):
    if i < N:
        mixed+=A[i]
    if i < M:
        mixed+=B[i]
    i+=1

nums = ''
for i in mixed:
    nums+=str(d[i])

while len(nums) > 2:
    tmp = ''
    for i in range(1,len(nums)):
        tmp+=str(int(nums[i-1])+int(nums[i]))[-1]
    nums = tmp

print(f'{int(nums)}%')
