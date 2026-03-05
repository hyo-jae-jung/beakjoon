from sys import stdin  

a,b = map(int,stdin.readline().strip().split("/"))

stack = []
while a/b != 1:
    if a/b > 1:
        a-=b
        a,b = b,a
        stack.append('R')
    elif a/b < 1:
        a,b = b,a
        a-=b
        stack.append('L')

print(''.join(stack))
