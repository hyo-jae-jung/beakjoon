import sys
from itertools import combinations as comb

answer_glob = []
for _ in range(int(sys.stdin.readline().strip())):
    answer_loc = 0
    temp = []
    for _ in range(int(sys.stdin.readline().strip())):
        temp.append(sys.stdin.readline().strip().split()[-1])

    for i in range(1,len(set(temp))+1):
        answer_loc+=len([j for j in comb(temp,i) if len(set(j))==i])

    answer_glob.append(answer_loc)

for i in answer_glob:
    print(i)
