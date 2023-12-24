from sys import stdin 
from bisect import bisect_left,bisect_right

N = int(stdin.readline().strip())
nums = sorted(list(map(int,''.join(map(str,range(1,N+1))))))
print(bisect_right(nums,3)-bisect_left(nums,3)+bisect_right(nums,6)-bisect_left(nums,6)+bisect_right(nums,9)-bisect_left(nums,9))
