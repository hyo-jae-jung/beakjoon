from sys import stdin 

N,S = map(int,stdin.readline().strip().split())
nums = list(map(int,stdin.readline().strip().split()))

nums_accum = [0]
for i in nums:
    nums_accum.append(nums_accum[-1]+i)

i,j=0,1
min_len = N+1

while j<=N:
    if nums_accum[j]-nums_accum[i] < S:
        j+=1
    else:
        min_len = min(min_len,j-i)
        i+=1
else:
    print(min_len if min_len < N+1 else 0)
    