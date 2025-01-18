from sys import stdin  

N = int(stdin.readline().strip())
B = list(map(int,stdin.readline().strip().split()))

plus_one_cnt = 0
double_cnt = 0

for i in B:
    if i:
        tmp_double_cnt = 0
        while i > 0:
            if i%2 == 1:
                plus_one_cnt+=1
                i-=1
            else:
                i = i//2
                tmp_double_cnt+=1
        double_cnt = max(double_cnt,tmp_double_cnt)

print(plus_one_cnt+double_cnt)
