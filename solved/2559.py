from sys import stdin 

N,K = map(int,stdin.readline().strip().split())
nums = [int(i) for i in stdin.readline().strip().split()]
sums = [0]
for i in nums:
    sums+=[sums[-1]+i]

candidated_answer = []
for i in range(K,len(nums)+1):
    candidated_answer.append(sums[i]-sums[i-K])

print(max(candidated_answer))
