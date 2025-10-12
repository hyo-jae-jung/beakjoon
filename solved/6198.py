from sys import stdin   

N = int(stdin.readline().strip())
stack = []
ans = 0
for _ in range(N):
    h = int(stdin.readline().strip())
    while stack and stack[-1] <= h:
        stack.pop()
    ans+=stack.__len__()
    stack.append(h)

print(ans)
