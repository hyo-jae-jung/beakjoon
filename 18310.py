from sys import stdin 

N = int(stdin.readline().strip())
house_loc_list = [int(i) for i in stdin.readline().strip().split()]
house_loc_set = sorted(list(set(house_loc_list)))

left = 0
right = len(house_loc_set)-1

def sum_distance(houses:list,antanna_house:int)->int:
    return sum([abs(i-houses[antanna_house]) for i in houses])

standard_min_loc = max(sum_distance(house_loc_list,left),sum_distance(house_loc_list,right))

while left < right:
    mid = (left+right)//2
    new_min_locs = [abs(i-house_loc_list[mid]) for i in house_loc_list]
    if new_min_locs < standard_min_loc:
        
