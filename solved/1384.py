from sys import stdin 

cnt = 1
answer = []
while (N := int(stdin.readline().strip())) > 0:
    members_and_messages = []
    group = [f"Group {cnt}\n"]
    for _ in range(N):
        members_and_messages.append(stdin.readline().strip().split())
    
    for i in range(N):
        for j in range(1,N):
            if members_and_messages[i][j] == 'N':
                group.append(f"{members_and_messages[(i-j)%N][0]} was nasty about {members_and_messages[i][0]}\n")
    
    if len(group) == 1:
        group.append("Nobody was nasty\n")
    
    cnt+=1
    answer.append(''.join(group))

print('\n'.join(answer))
