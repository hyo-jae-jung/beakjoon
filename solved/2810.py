from sys import stdin 

_ = int(stdin.readline().strip())
sit = list(stdin.readline().strip())
s_cnt,l_cnt = 0,0
for i in sit:
    if i == 'S':
        s_cnt+=1
    else:
        l_cnt+=1

print((s_cnt+l_cnt//2) + (1 if l_cnt else 0))
