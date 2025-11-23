from sys import stdin  

N = int(stdin.readline().strip())
board = [list(map(int,stdin.readline().strip().split())) for _ in range(N)]

ans = float('inf')
total_people = set(range(N))
pre_people = set(range(N))
start_team_members = []

def solution(cnt=0,idx=0):
    global N,board,ans,pre_people,total_people

    if cnt == N//2:

        start_team_members = list(total_people - pre_people)
        link_team_members = list(pre_people)
        start_team_val,link_team_val = 0,0

        for i in range(N//2):
            for j in range(1+i,N//2):
                start_team_val+=board[start_team_members[i]][start_team_members[j]] + board[start_team_members[j]][start_team_members[i]]
                link_team_val+=board[link_team_members[i]][link_team_members[j]] + board[link_team_members[j]][link_team_members[i]]

        ans = min(ans,abs(start_team_val - link_team_val))
        return 
    
    for k in range(idx,N):
        if k in pre_people:
            pre_people.remove(k)
            solution(cnt+1,k+1)
            pre_people.add(k)

solution()
print(ans)
