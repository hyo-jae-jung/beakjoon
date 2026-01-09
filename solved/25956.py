from sys import stdin   

N = int(stdin.readline().strip())
L = [0]
for _ in range(N):
    L.append(int(stdin.readline().strip()))

ans = [0]*(N+1)
stack = {}
prev_lev = 0
for i,l in enumerate(L):

    while prev_lev > l:
        ans[stack[prev_lev - 1][-1]] = len(stack[prev_lev])
        stack.pop(prev_lev)
        prev_lev-=1

    if prev_lev == l or prev_lev + 1 == l:
        prev_lev = l
        if not stack.get(prev_lev):
            stack.update({prev_lev:[]})
        stack[prev_lev].append(i)
        continue

    if prev_lev + 1 < l:
        ans = [0,-1]
        break
    
if ans[1] != -1:
    while prev_lev > 0:
        ans[stack[prev_lev - 1][-1]] = len(stack[prev_lev])
        stack.pop(prev_lev)
        prev_lev-=1

print(*ans[1:],sep='\n')
