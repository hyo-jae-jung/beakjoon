from sys import stdin 

cups = [1,0,0]
mix = stdin.readline().strip()
for i in mix:
    if i == 'A':
        cups[0],cups[1] = cups[1],cups[0]
    elif i == 'B':
        cups[2],cups[1] = cups[1],cups[2]
    else:
        cups[2],cups[0] = cups[0],cups[2]

print(cups.index(1)+1)
