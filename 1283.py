from sys import stdin 

N = int(stdin.readline().strip())

S = []
answer_list = []
for _ in range(N):
    temp = stdin.readline().strip().split()
    answer = []
    for i in temp:
        if i[0] not in S:
            S.append(i[0])
            answer.append('['+i[0]+']'+i[1:])
        else:
            answer.append(i)
            