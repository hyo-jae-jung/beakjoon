from sys import stdin  

S = stdin.readline().strip()

stack = []
for i in S:
    b = 0
    while stack and str(stack[-1]).isdigit():
        b+=stack.pop()
    
    if not stack and i in [')',']']:
        ans = 0
        break

    if stack and stack[-1] == '(' and i == ']':
        ans = 0
        break

    if stack and stack[-1] == '[' and i == ')':
        ans = 0
        break

    if stack and stack[-1] == '(' and i == ')':
        stack.pop()
        stack.append(2*(1 if b == 0 else b))
        continue

    if stack and stack[-1] == '[' and i == ']':
        stack.pop()
        stack.append(3*(1 if b == 0 else b))
        continue
    
    if b > 0:
        stack.append(b)
    stack.append(i)

else:
    for s in stack:
        if not str(s).isdigit():
            ans = 0
            break
    else:
        ans = sum(stack)

print(ans)
