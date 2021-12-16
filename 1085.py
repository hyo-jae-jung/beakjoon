import sys

x,y,w,h = map(int,sys.stdin.readline().split())

from_xy_to_borders_list = []

from_xy_to_borders_list.append(x)
from_xy_to_borders_list.append(y)
from_xy_to_borders_list.append(w-x)
from_xy_to_borders_list.append(h-y)

print(min(from_xy_to_borders_list))