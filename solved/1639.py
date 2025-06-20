from sys import stdin   

prefix_sum = [0]
for i in map(int,list(stdin.readline().strip())):
    prefix_sum.append(prefix_sum[-1] + i)

def solution():
    n = len(prefix_sum) - 1
    for i in range(n//2,-1,-1):
        for j in range(2*i,n+1):
            if prefix_sum[j] - prefix_sum[j-i] == prefix_sum[j-i] - prefix_sum[j-2*i]:
                return 2*i
            
print(solution())
