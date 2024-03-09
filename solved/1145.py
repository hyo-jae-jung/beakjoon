from sys import stdin 
from itertools import combinations as comb 
from math import lcm

nums = list(map(int,stdin.readline().strip().split()))

mult_nums = []

for i,j,k in comb([0,1,2,3,4],3):
    mult_nums.append(lcm(nums[i],nums[j],nums[k]))

print(min(mult_nums))
