from sys import stdin 
from collections import defaultdict

N = int(stdin.readline().strip())

original = []
for _ in range(N):
    original.append(stdin.readline().strip())

alphabet_set = set()

for i in original:
    for j in i:
        alphabet_set.add(j)
        
d = defaultdict(list)

for i in alphabet_set:
    d[i] = [0]*8

for k in original:
    for i,j in enumerate(k.rjust(8,'0')):
        if j != '0':
            d[j][i]+=1

def diff_raise(x:list)->int:
    answer = 0
    for i,j in enumerate(reversed(x)):
        answer+=j*10**i
    return answer

d_list  = []
for i,j in d.items():
    d_list.append((i,diff_raise(j)))

d_list.sort(key=lambda x:-x[1])

answer_chart = defaultdict(int)

for i,j in zip(range(9,9-len(d_list),-1),d_list):
    answer_chart[j[0]] = str(i)

answer = 0
for i in original:
    temp = ''
    for j in i:
        temp+=answer_chart[j]
    answer+=int(temp)

print(answer)
