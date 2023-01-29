from sys import stdin 

N = int(stdin.readline().strip())
work_table = [[],[],[],[]]
for _ in range(N):
    for i in range(4):
        work_table[i].extend([i for i in stdin.readline().strip().split() if i != '-'])

soldiers_d = dict.fromkeys(set(sum(work_table,[])),0)
work_time = [4,6,4,10]

for i,j in zip(work_table,work_time):
    for k in i:
        soldiers_d[k]+=j

try:
    if max(soldiers_d.values()) - min(soldiers_d.values()) <= 12:
        print('Yes')
    else:
        print('No')
except:
    print('Yes')
