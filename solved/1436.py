import sys

N = int(sys.stdin.readline().strip())
end_num_cnt = 0
num = 0
while end_num_cnt<N:
    num+=1
    if '666' in str(num):
        end_num_cnt+=1

print(num)
