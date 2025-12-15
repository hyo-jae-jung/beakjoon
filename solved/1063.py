from sys import stdin 

king,stone,N = stdin.readline().strip().split()
board = [[0]*8 for _ in range(8)]

def shift(x,y,dx,dy):
    global board
    board[y][x],board[y+dy][x+dx] = board[y+dy][x+dx],board[y][x]
    return x+dx,y+dy

d = {}
d.update({'R':[0,1]})
d.update({'L':[0,-1]})
d.update({'B':[1,0]})
d.update({'T':[-1,0]})
d.update({'RT':[-1,1]})
d.update({'LT':[-1,-1]})
d.update({'RB':[1,1]})
d.update({'LB':[1,-1]})

king_colume,king_row = list(king)
stone_colume,stone_row = list(stone)

board[king_y:=(8-int(king_row))][king_x:=(ord(king_colume)-65)] = 'K'
board[stone_y:=(8-int(stone_row))][stone_x:=(ord(stone_colume)-65)] = 'S'

for _ in range(int(N)):
    move = stdin.readline().strip()
    dy,dx = d[move]
    ny=king_y+dy
    nx=king_x+dx
    if any([0 > ny,8 <= ny,0 > nx,8 <= nx]):
        continue

    if board[ny][nx] == 'S':
        if 0 <= stone_y+dy < 8 and 0 <= stone_x+dx < 8:
            stone_x,stone_y = shift(stone_x,stone_y,dx,dy)
        else:
            continue
    
    king_x,king_y = shift(king_x,king_y,dx,dy)

print(str(chr(king_x+65))+str(8-king_y))
print(str(chr(stone_x+65))+str(8-stone_y))
