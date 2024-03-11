from sys import stdin 

N = int(stdin.readline().strip())

scores = {i:[0]*3 for i in range(1,4)}
for _ in range(N):
    for i,j in zip(range(1,4),map(int,stdin.readline().strip().split())):
        scores[i][j-1]+=1

second,first = sorted(scores.items(),key=lambda x:(x[1][0]*1+x[1][1]*2+x[1][2]*3,x[1][2],x[1][1]))[1:]
first_score = first[1][0]*1+first[1][1]*2+first[1][2]*3
if first[1] == second[1]:
    print(0,first_score)
else:
    print(first[0],first_score)
