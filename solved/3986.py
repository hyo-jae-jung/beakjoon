from sys import stdin  

N = int(stdin.readline().strip())
ans = 0

def solution(s):
    stack = [s[0]]
    for i in s[1:]:    
        if stack == [] or i != stack[-1]:
            stack.append(i)
        else:
            stack.pop()

    if stack:
        return 0
    else:
        return 1


for _ in range(N):
    ans+=solution(stdin.readline().strip())

print(ans)
