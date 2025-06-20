from sys import stdin  

t = int(stdin.readline().strip())
ans = []
for _ in range(t):
    lt,wt,le,we = map(int,stdin.readline().strip().split())
    if lt*wt > le*we:
        ans.append("TelecomParisTech")
    elif lt*wt < le*we:
        ans.append("Eurecom")
    else:
        ans.append("Tie")

print(*ans,sep='\n')
