from sys import stdin  

t = int(stdin.readline().strip())
ans = []
for _ in range(t):
    p1s,p2s = 0,0
    n = int(stdin.readline().strip())
    for _ in range(n):
        tmp = stdin.readline().strip()
        if tmp == 'R P':
            p2s+=1
        elif tmp == 'P R':
            p1s+=1
        elif tmp == 'R S':
            p1s+=1
        elif tmp == 'S R':
            p2s+=1
        elif tmp == 'P S':
            p2s+=1
        elif tmp == 'S P':
            p1s+=1
    if p1s > p2s:
        ans.append("Player 1")
    elif p1s < p2s:
        ans.append("Player 2")
    else:
        ans.append("TIE")

print(*ans,sep='\n')
