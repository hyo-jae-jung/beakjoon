cases = []

for y in range(3):
    for x in range(3):
        tmp = 2**(x+3*y)
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            if 0 <= (nx:=x+dx) < 3 and 0 <= (ny:=y+dy) < 3:
                tmp+=2**(nx+3*ny)
        cases.append(tmp)

def solution(pre_board=0,pre_cnt=0,idx=0):
    global result_board,cases,visited,ans_cnt
    if result_board == pre_board:
        ans_cnt = min(ans_cnt,pre_cnt)
        return
    
    if pre_cnt < ans_cnt:
        for i in range(idx,9):
            if not visited[i]:
                visited[i] = True
                solution(pre_board^cases[i],pre_cnt+1,i+1)
                visited[i] = False

from sys import stdin  

P = int(stdin.readline().strip())
ans = []
for _ in range(P):
    visited = [False]*9
    result_board = 0
    ans_cnt = float('inf')

    for i in range(3):
        for j,k in enumerate(list(stdin.readline().strip())):
            if k == '*':
                result_board+=2**(j+i*3)

    solution()
    ans.append(ans_cnt)

print(*ans,sep='\n')
