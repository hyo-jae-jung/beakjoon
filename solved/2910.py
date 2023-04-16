from sys import stdin 
from collections import defaultdict

N,C = map(int,stdin.readline().strip().split())
arr = map(int,stdin.readline().strip().split())

hash_map = defaultdict(list)

num_sort = 0
for i in arr:
    if not hash_map[i]:
        hash_map[i] = [num_sort,1]
        num_sort+=1
    else:
        hash_map[i][1]+=1

temp = []

for i,j in hash_map.items():
    j.append(i)
    temp.append(j)

answer = []

for _,i,j in sorted(temp,key=lambda x:(-x[1],x[0])):
    answer.extend([j]*i)

print(*answer)
