from sys import stdin 

M = int(stdin.readline().strip())
S = set()
check = ''
for _ in range(M):
    inp = stdin.readline().strip().split()
    if inp[0] == 'add':
        S = S | set([int(inp[1])])
    elif inp[0] == 'remove':
        S = S ^ set([int(inp[1])])
    elif inp[0] == 'check':
        if set([int(inp[1])]) & S:
            check+='1'
        else:
            check+='0'
    elif inp[0] == 'toggle':
        if set([int(inp[1])]) & S:
            S = S ^ set([int(inp[1])])
        else:
            S = S | set([int(inp[1])])
    elif inp[0] == 'all':
        S = set(range(1,21))
    elif inp[0] == 'empty':
        S = set()

for i in check:
    print(i)
    