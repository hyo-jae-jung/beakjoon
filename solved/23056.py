from sys import stdin  
from collections import defaultdict

N,M = map(int,stdin.readline().strip().split())

even,odd = [],[]

m_cnt = defaultdict(int)

while (s:=stdin.readline().strip()) != '0 0':
    class_num,student_name = s.split()
    
    if m_cnt[class_num] < M:
        m_cnt[class_num]+=1
        if int(class_num)%2 == 0:
            even.append((int(class_num),student_name))
        else:
            odd.append((int(class_num),student_name))

odd.sort(key=lambda x:(x[0],len(x[1]),x[1]))
even.sort(key=lambda x:(x[0],len(x[1]),x[1]))

for i in odd:
    print(*i)
for i in even:
    print(*i)
