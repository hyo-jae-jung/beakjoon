from sys import stdin 

N = int(stdin.readline().strip())
stairs = []
for _ in range(N):
    stairs.append(int(stdin.readline().strip()))

memo = [[0,0] for _ in range(300)]

def max_score(floor_idx=N-1,stack=1):
    
    if memo[floor_idx][stack-1]:
        return memo[floor_idx][stack-1]
    
    if floor_idx < 0:
        return 0
    
    memo[floor_idx][stack-1] = stairs[floor_idx] + max_score(floor_idx-2,1)
    
    if stack < 2:
        memo[floor_idx][stack-1] = max(memo[floor_idx][stack-1],stairs[floor_idx] + max_score(floor_idx-1,stack+1))
    return memo[floor_idx][stack-1]

print(max_score())
