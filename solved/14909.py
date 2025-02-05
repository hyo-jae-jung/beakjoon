from sys import stdin   
from bisect import bisect_left

arr = list(map(int,stdin.readline().strip().split()))
arr.sort()
print(len(arr[bisect_left(arr,1):]))
