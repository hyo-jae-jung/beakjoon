import sys
from collections import deque

K = int(sys.stdin.readline().strip())

hexagon_items = deque()
for _ in range(6):
    d, m = map(int,sys.stdin.readline().strip().split())
    hexagon_items.append((d,m))

d = dict.fromkeys([1,2,3,4],0)

for i,_ in hexagon_items:
    d[i]+=1
large_square_d = [i for i,j in hexagon_items if d[i]==1]

while not all([hexagon_items[0][0] in large_square_d, hexagon_items[1][0] in large_square_d]):
    hexagon_items.rotate(1)

large_square_items = [j for i,j in hexagon_items if d[i]==1]
small_square_items = [j for i,j in hexagon_items if d[i]==2]

large_square_area = large_square_items[0]*large_square_items[1]
small_square_area = small_square_items[1]*small_square_items[2]
hexagon_area = large_square_area-small_square_area

print(hexagon_area*K)
