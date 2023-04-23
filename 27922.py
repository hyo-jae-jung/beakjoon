from sys import stdin 

N,K = map(int,stdin.readline().strip().split())
lactures_abilites = []
for _ in range(N):
    lactures_abilites.append(tuple(map(int,stdin.readline().strip().split())))

from itertools import permutations as perm
answer = 0
for i,j,k in perm([0,1,2],3):
    temp = [0,0,0]
    for l,m,n in sorted(lactures_abilites,key=lambda x:(x[i],x[j],x[k]))[:K]:
        temp[0]+=l
        temp[1]+=m
        temp[2]+=n
    if answer < (temp_ans := sum(sorted(temp)[1:])):
        answer = temp_ans
    
print(answer)
