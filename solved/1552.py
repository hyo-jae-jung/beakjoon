def check_cycle(arr,n):
    cnt = 0
    visited = [True]*n
    #dfs
    for i in range(n):
        if visited[i]:
            j = i
            visited[j] = False
            while visited[j:=arr[j]]:
                visited[j] = False
            cnt+=1
    return cnt

from sys import stdin  

N = int(stdin.readline().strip())
domino_table = [list(stdin.readline().strip()) for _ in range(N)]
min_val,max_val = float('inf'),-float('inf')
col_visited = 0
row_visited = 0
arr = []

def solution(val=1,cnt=0):
    global N,domino_table,min_val,max_val,col_visited,row_visited,arr
    if cnt == N:
        cycle_val = 1 if check_cycle(arr,N)%2 == 1 else -1
        min_val = min(min_val,val*cycle_val)
        max_val = max(max_val,val*cycle_val)
        return
    
    row_visited+=(1 << cnt)
    for j in range(N):
        if col_visited & (1 << j) == 0:
            col_visited+=(1 << j)
            dval = domino_table[cnt][j]
            if dval.isnumeric():
                dval = int(dval)
            else:
                dval = (ord(dval)-64)*(-1)
            new_val = val*dval
            arr.append(j)
            solution(new_val,cnt+1)
            arr.pop()
            col_visited-=(1 << j)
    row_visited-=(1 << cnt)

solution()
print(min_val)
print(max_val)
