from sys import stdin  

R,C = map(int,stdin.readline().strip().split())
arr = []
for _ in range(R):
    arr.append(list(stdin.readline().strip()))

ans = 0

memo = [[True]*C for _ in range(R)]

def solution(r,c):
    if memo[r][c] == False:
        return False 
    
    if arr[r][c] == '.':
        return False

    memo[r][c] = False
    if r-1 >= 0:
        solution(r-1,c)
    if r+1 < R:
        solution(r+1,c)
    if c-1 >= 0:
        solution(r,c-1)
    if c+1 < C:
        solution(r,c+1)

for i in range(R):
    for j in range(C):
        if memo[i][j]:
            if arr[i][j] == '#':
                ans+=1
                solution(i,j)

print(ans)
