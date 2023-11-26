from sys import stdin 

n = int(stdin.readline().strip())
ans = []
for _ in range(n):
    p = int(stdin.readline().strip())
    best_player = (0,None)
    for _ in range(p):
        price,player = stdin.readline().strip().split()
        if int(price) > best_player[0]:
            best_player = (int(price),player)
    ans.append(best_player[1])

print(*ans,sep='\n')
