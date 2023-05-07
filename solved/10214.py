from sys import stdin 

T = int(stdin.readline().strip())

answer = []

for _ in range(T):
    
    Yonsei,Korea = 0,0
    for _ in range(9):
        Y,K = map(int,stdin.readline().strip().split())
        Yonsei+=Y
        Korea+=K
    else:
        if Yonsei > Korea:
            answer.append('Yonsei')
        elif Yonsei < Korea:
            answer.append('Korea')
        else:
            answer.append('Draw')

print(*answer,sep='\n')
