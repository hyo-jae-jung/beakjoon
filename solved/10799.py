from sys import stdin
from bisect import bisect_left, bisect_right

inp = stdin.readline().strip()

temp = []
steck = 0
bar_list = []
laser_list = []

for i,j in enumerate(inp):
    if j == '(':
        temp.append(i)
    else:
        k = temp.pop()
        if i-k > 1:
            bar_list.append((k,i))
        else:
            laser_list.append(k)

answer = 0

def cnt_within_range (arr, left_v, right_v):
    left_idx = bisect_left(arr, left_v)
    right_idx = bisect_right(arr, right_v)
    return right_idx - left_idx

for i,j in bar_list:
    answer+=cnt_within_range(laser_list,i,j)+1

print(answer)
