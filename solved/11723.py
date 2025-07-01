from sys import stdin 

M = int(stdin.readline().strip())

ans = 0
for _ in range(M):
    inp = stdin.readline().strip().split()
    if inp[0] == 'add':
        ans = ans|1<<(int(inp[1]) - 1)
    elif inp[0] == 'check':
        print('1' if ans&(1<<(int(inp[1]) - 1)) else '0')
    elif inp[0] == 'remove':
        if ans&(1<<(int(inp[1]) - 1)):
            ans = ans^1<<(int(inp[1]) - 1)
    elif inp[0] == 'toggle':
        ans = ans^(1<<(int(inp[1]) - 1))
    elif inp[0] == 'all':
        ans = (1<<20) - 1
    elif inp[0] == 'empty':
        ans = 0
