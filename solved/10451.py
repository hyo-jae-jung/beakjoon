from sys import stdin 

T = int(stdin.readline().strip())

answer = []

for _ in range(T):
    N = int(stdin.readline().strip())
    permutation = [0] + list(map(int,stdin.readline().strip().split()))
    memoization = [False]*(N+1)

    cnt = 0
    for i in range(1,N+1):
        if memoization[i] == False:    
            memoization[i] = True
            temp = i
            while True:
                temp = permutation[temp]
                memoization[temp] = True
                if i == temp:
                    cnt+=1
                    break
    else:
        answer.append(cnt)
    
print(*answer,sep='\n')
