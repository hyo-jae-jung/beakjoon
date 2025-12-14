from sys import stdin  

n,W = map(int,stdin.readline().strip().split())
S = [int(stdin.readline().strip()) for _ in range(n)]

stack = [S[0]]

for i in range(1,n):
    if stack[-1] < S[i]:
        stack.append(S[i])
        continue

    if stack[-1] > S[i]:
        if len(stack) > 1:
            cnt = W//stack[0]
            W+=(stack[-1] - stack[0])*cnt
        stack = [S[i]]
        continue
else:
    if len(stack) > 1:
        cnt = W//stack[0]
        W+=(stack[-1] - stack[0])*cnt

print(W)
