from sys import stdin  

A,B = stdin.readline().strip().split()
A_len = A.__len__()
visited = [False]*A_len
ans = -1

def solution(cnt=0,val=''):
    global A,B,ans,A_len
    if cnt == A_len and int(val) < int(B):
        ans = max(ans,int(val))
        return

    for i in range(A_len):
        if not visited[i]:
            if val == '' and A[i] == '0':
                continue
            
            if int(val+A[i]+'0'*(A_len - (cnt + 1))) > int(B):
                continue

            visited[i] = True
            solution(cnt+1,val+A[i])
            visited[i] = False

solution()
print(ans)
