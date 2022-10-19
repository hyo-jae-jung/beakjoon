Y,X = map(int,input().split())
board = []
for i in range(Y):    
    board.extend(list(input()))

def chess_board(first_color:str)->list:

    chess_board = []
    color_num ={'B':0,'W':1}
    one_line = ['B','W','B','W','B','W','B','W']
    one_line_reverse = list(reversed(one_line))

    for i in range(8):
        if i%2 == color_num[first_color]:
            chess_board.extend(one_line)
        else:
            chess_board.extend(one_line_reverse)
    return  chess_board
    
chess_board_B = chess_board('B')
chess_board_W = chess_board('W')

for i in range(X-7):
    for j in range(Y-7):
        chess_board_sample = []
        for k in range(1,9):
            chess_board_sample.extend(board[(8+(X-8))*(k-1)+X*(Y-8):(8+(X-8))*(k)+X*(Y-8)])
        print(chess_board_sample)
