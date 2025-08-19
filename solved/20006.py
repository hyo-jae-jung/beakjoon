from sys import stdin  

p,m = map(int,stdin.readline().strip().split())
rooms = []
for _ in range(p):
    lev,name = stdin.readline().strip().split()

    if not rooms:
        rooms.append([(int(lev),name)])
        continue

    i = 0
    while len(rooms) > i:
        if len(rooms[i]) < m and rooms[i][0][0]-10 <= int(lev) <= rooms[i][0][0]+10:
            rooms[i].append((int(lev),name))
            break
        i+=1
    else:
        rooms.append([(int(lev),name)])

for room in rooms:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")
    
    for user in sorted(room,key=lambda x:(x[1])):
        print(*user)

