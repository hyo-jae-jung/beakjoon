import sys
N,M = map(int,sys.stdin.readline().strip().split())
input_board = [sys.stdin.readline().strip() for _ in range(N)]
first_color = 'B'
def cnt_board(board,first_color):
    answer = []
    for i,j in enumerate(board):
        temp = []
        for k,l in enumerate(j):
            if i%2 == 0:
                if k%2 == 0:
                    if l == first_color:
                        temp.append(0)
                    else:
                        temp.append(1)
                else:
                    if l != first_color:
                        temp.append(0)
                    else:
                        temp.append(1)
            else:
                if k%2 != 0:
                    if l == first_color:
                        temp.append(0)
                    else:
                        temp.append(1)
                else:
                    if l != first_color:
                        temp.append(0)
                    else:
                        temp.append(1)
        answer.append(temp)
    return answer

answer = []
for i in range(N-7):
    for j in range(M-7):
        


if __name__ == "__main__":
    print(cnt_board(input_board,first_color))
