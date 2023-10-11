from sys import stdin 

T = int(stdin.readline().strip())
answer = []
for _ in range(T):
    X,Y = map(int,stdin.readline().strip().split())
    xs = int(''.join(list(map(str,stdin.readline().strip().split()))))
    ys = int(''.join(list(map(str,stdin.readline().strip().split()))))
    rotate_board = list(map(str,stdin.readline().strip().split()))

    win_cases = []
    for i in range(X):
        num = ''
        for j in range(Y):
            num+=rotate_board[(i+j)%X]
        if xs <= int(num) <= ys:
            win_cases.append(num)
    
    answer.append(len(win_cases))

print(*answer,sep='\n')
