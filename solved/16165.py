from sys import stdin 

N,M = map(int,stdin.readline().strip().split())
data = {}
for _ in range(N):
    team_name = stdin.readline().strip()
    team_member_cnt = int(stdin.readline().strip())
    team_members = []
    for _ in range(team_member_cnt):
        team_member = stdin.readline().strip()
        team_members.append(team_member)
        data.update({team_member:team_name})
    team_members.sort()

    data.update({team_name:team_members})

ans = []
for _ in range(M):
    name = stdin.readline().strip()
    q_num = int(stdin.readline().strip())
    if q_num == 1:
        ans.append(data[name])
    elif q_num == 0:
        for member_name in data[name]:
            ans.append(member_name)
            
print(*ans,sep='\n')
