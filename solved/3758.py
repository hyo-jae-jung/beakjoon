from sys import stdin   

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    n,k,t,m = map(int,stdin.readline().strip().split())

    score_board = [[[0]*k,0,0,i] for i in range(1,n+1)]

    for idx in range(m):
        i,j,s = map(int,stdin.readline().strip().split())
        score_board[i-1][0][j-1] = max(score_board[i-1][0][j-1],s)
        score_board[i-1][1]+=1
        score_board[i-1][2] = idx

    score_board.sort(key=lambda x:(-sum(x[0]),x[1],x[2]))

    for i,j in enumerate(score_board,1):
        if j[-1] == t:
            ans.append(i)
            break

print(*ans,sep='\n')

