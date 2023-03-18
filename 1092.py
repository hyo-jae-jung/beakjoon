from sys import stdin 
from collections import defaultdict 

crane_cnt = int(stdin.readline().strip())
cranes = [int(i) for i in stdin.readline().strip().split()]
box_cnt = int(stdin.readline().strip())
boxs = [int(i) for i in stdin.readline().strip().split()]

set_cranes = sorted(list(set(cranes)))

crane_dict = dict.fromkeys(set(cranes),0)
box_dict = dict.fromkeys(set(cranes),0)

print(crane_dict)
print(box_dict)

for i in cranes:
    crane_dict[i]+=1

for i in boxs:
    for j in set_cranes:
        if i<=j:
            box_dict[j]+=1
            break

print(crane_dict)
print(box_dict)
