from sys import stdin 

AB = stdin.readline().strip()
if AB[1] == '0':
    print(int(AB[:2])+int(AB[2:]))
else:
    print(int(AB[:1])+int(AB[1:]))
    