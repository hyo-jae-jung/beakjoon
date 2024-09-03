from sys import stdin  

first_player = int(stdin.readline().strip())
player1 = set()
player2 = set()
ans = 0

def check_win(arr):
    
    if not(set([(1,1),(1,2),(1,3)]) - arr):
        return "win"
    if not(set([(2,1),(2,2),(2,3)]) - arr):
        return "win"
    if not(set([(3,1),(3,2),(3,3)]) - arr):
        return "win"
    if not(set([(1,1),(2,1),(3,1)]) - arr):
        return "win"
    if not(set([(1,2),(2,2),(3,2)]) - arr):
        return "win"
    if not(set([(1,3),(2,3),(3,3)]) - arr):
        return "win"
    if not(set([(1,1),(2,2),(3,3)]) - arr):
        return "win"
    if not(set([(1,3),(2,2),(3,1)]) - arr):
        return "win"
    
for i in range(9):
    if (i+first_player)%2 == 0:
        player2.add(tuple(map(int,stdin.readline().strip().split())))
    else:
        player1.add(tuple(map(int,stdin.readline().strip().split())))

    if ans == 0:
        if check_win(player1) == 'win':
            ans = 1
        elif check_win(player2) == 'win':
            ans = 2

print(ans)
