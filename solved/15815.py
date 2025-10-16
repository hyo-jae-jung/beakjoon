from sys import stdin  

S = stdin.readline().strip()
stack = []
sign = set(["+","-","*","/"])
for s in S:
    if s in sign:
        b = stack.pop()
        a = stack.pop()
        if s == "/":
            s+=s
        stack.append(str(eval(a+s+b)))
    else:
        stack.append(s)

print(*stack)
