from sys import stdin  

n,p,m = map(int,stdin.readline().strip().split())

scoreboard = {}
for _ in range(n):
    scoreboard.update({stdin.readline().strip():0})

ans = []
for _ in range(m):
    name,score = stdin.readline().strip().split()
    if scoreboard.get(name) >= p:
        continue

    scoreboard[name]+=int(score)
    if scoreboard.get(name) >= p:
        ans.append(f"{name} wins!")
        
if ans:
    print(*ans,sep='\n')
else:
    print("No winner!")
