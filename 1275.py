from sys import stdin 

N,Q = map(int,stdin.readline().strip().split())
nums = {i:int(j) for i,j in enumerate(stdin.readline().strip().split(),1)}
answer = []
for _ in range(Q):
    x,y,a,b = map(int,stdin.readline().strip().split())
    answer.append(sum([nums[i] for i in range(min(x,y),max(x,y)+1)]))
    nums[a]=b

print(*answer, sep='\n')
