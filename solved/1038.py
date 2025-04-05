from sys import stdin 

N = int(stdin.readline().strip())

if N > 1022:
    print(-1)
else:
    i=0
    stack = list(range(10))
    while len(stack) <= N:
        for j in range(int(str(stack[i])[-1])):
            stack.append(int(str(stack[i])+str(j)))
        i+=1

    print(stack[N])
