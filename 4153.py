import sys

triangles_list = []

while True:
    x,y,z = map(int,sys.stdin.readline().split())
    triangle = [x,y,z]
    if sum(triangle) != 0:
        triangles_list.append(triangle)
    else:
        break

for i in triangles_list:
    i.sort()
    if i[2]**2 == i[0]**2 + i[1]**2:
        print("right")
    else:
        print("wrong")