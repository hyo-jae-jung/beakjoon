import sys
from bisect import bisect_left, bisect_right

N = int(sys.stdin.readline().strip())
N_list = sorted([int(i) for i in sys.stdin.readline().strip().split()])
M = int(sys.stdin.readline().strip())
M_list = [int(i) for i in sys.stdin.readline().strip().split()]

def cnt_within_range(arr, left_v, right_v):
    left_idx = bisect_left(arr, left_v)
    right_idx = bisect_right(arr, right_v)
    return right_idx - left_idx

d = dict.fromkeys(M_list,0)

for i in  set(N_list) & set(M_list):
    d[i] = cnt_within_range(N_list,i,i)

answer = []

for i in M_list:
    answer.append(d[i])

print(*answer)
