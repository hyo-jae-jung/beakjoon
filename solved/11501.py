def solution(n,arr):
    result = 0
    stack = [arr[-1]]
    arr.pop()
    while arr:
        v = arr.pop()
        if stack[0] <= v:
            result+=stack[0]*len(stack) - sum(stack)
            stack = [v]
        else:
            stack.append(v)
    result+=stack[0]*len(stack) - sum(stack)
    return result

from sys import stdin   

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    n = int(stdin.readline().strip())
    arr = list(map(int,stdin.readline().strip().split()))
    ans.append(solution(n,arr))

print(*ans,sep='\n')
