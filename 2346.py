from sys import stdin 

N = int(stdin.readline().strip())
nums = [int(i) for i in stdin.readline().strip().split()]
answer = [1]
idx = 0

while nums:
    tmp_idx = (idx+nums[idx])%N
    print(idx,tmp_idx,nums)
    if idx < tmp_idx:
        tmp_idx-=1
    del nums[idx]
    N-=1
    idx=tmp_idx

print(answer)
