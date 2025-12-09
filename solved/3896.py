from sys import stdin   
from bisect import bisect_left

T = int(stdin.readline().strip())
ans = []

prime_nums = []
min_prime = [0]*1299710
idx = 2
while idx <= 1299709:
    if min_prime[idx] == 0:
        min_prime[idx] = idx
        prime_nums.append(idx)

    for p in prime_nums:
        if p > min_prime[idx] or idx*p > 1299709:
            break
        min_prime[idx*p] = p

    idx+=1

for _ in range(T):
    k = int(stdin.readline().strip())
    idx = bisect_left(prime_nums,k)
    if prime_nums[idx] == k:
        print(0)
    else:
        print(prime_nums[idx] - prime_nums[idx-1])
