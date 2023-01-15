from sys import stdin 

N,M = map(int,stdin.readline().strip().split())
nums = [int(i) for i in stdin.readline().strip().split()]
prob = []
nums_list = []
for _ in range(M):
    prob.append(tuple(int(i) for i in stdin.readline().strip().split()))
    nums_list.append(nums)

for i,j in enumerate(prob):
    a,b = j
    a-=1
    b-=1
    del nums_list[i][b+1:]
    del nums_list[i][:a]
    print(nums_list[i])
    print(sum(nums_list[i]))

    
