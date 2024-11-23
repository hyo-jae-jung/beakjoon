from sys import stdin  

f = stdin.readline().strip()
f = f.split('x')
f.pop()

if f:
    if f[0] == '':
        print(1)
    elif f[0] == '-':
        print(-1)
    else:
        print(f[0])
else:
    print(0)
