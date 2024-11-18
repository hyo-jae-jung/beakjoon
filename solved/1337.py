from sys import stdin  

N = int(stdin.readline().strip())
s = set()
for _ in range(N):
    s.add(int(stdin.readline().strip()))

max_glob_right_arr_cnt = 0

for i in s:
    max_loc_right_arr_cnt = 1
    for j in range(i+1,i+5):
        if j in s:
            max_loc_right_arr_cnt+=1
    max_glob_right_arr_cnt = max(max_glob_right_arr_cnt,max_loc_right_arr_cnt)

print(5 - max_glob_right_arr_cnt)
