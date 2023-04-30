from sys import stdin 

string = stdin.readline().strip()

answer = 0
direction = ''

for i in string:
    if i == direction:
        answer+=5
    else:
        answer+=10
    direction = i

print(answer)
