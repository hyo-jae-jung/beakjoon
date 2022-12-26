import sys

N,M = map(int,sys.stdin.readline().strip().split())
input_board = [sys.stdin.readline().strip() for _ in range(N)]

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
def cnt_sum(cnt_board,N,M):
    answer=[]
    for i in range(N-7):
        for j in range(M-7):
            temp = 0
            for k in cnt_board[0+i:8+i]:
                temp+=sum(k[0+j:8+j])
            answer.append(temp)
    return answer
cnt_board_B = cnt_board(input_board,'B')
cnt_board_W = cnt_board(input_board,'W')
sum_B = cnt_sum(cnt_board_B,N,M)
sum_W = cnt_sum(cnt_board_W,N,M)

if __name__ == "__main__":
            
    print(min(sum_W+sum_B))
