import sys

coordinates_list = []
for _ in range(3):
    x,y = map(int,sys.stdin.readline().split())
    x_y_coordinates = [x,y]
    coordinates_list.append(x_y_coordinates)

answer_x_y_coordinates = []

for i in range(0,2):
    if coordinates_list[0][i] == coordinates_list[1][i]:
        answer_x_y_coordinates.append(coordinates_list[2][i])
    elif coordinates_list[0][i] == coordinates_list[2][i]:
        answer_x_y_coordinates.append(coordinates_list[1][i])
    else:
        answer_x_y_coordinates.append(coordinates_list[0][i])

print(f"{answer_x_y_coordinates[0]} {answer_x_y_coordinates[1]}")