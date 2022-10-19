N = int(input())

dungchi = [tuple(map(int,input().split())) for _ in range(N)]
man_cnt = len(dungchi)
dungchi_score = [1]*N

for i in range(man_cnt):
    for j in range(i+1,man_cnt):
        if dungchi[i][0] > dungchi[j][0] and dungchi[i][1] > dungchi[j][1]:
            dungchi_score[j] += 1
        elif dungchi[i][0] < dungchi[j][0] and dungchi[i][1] < dungchi[j][1]:
            dungchi_score[i] += 1

print(' '.join(map(str,[i for i in dungchi_score])))

