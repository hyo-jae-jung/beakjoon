from sys import stdin  

A = int(stdin.readline().strip())
T = int(stdin.readline().strip())
chant = stdin.readline().strip()

bbun,degi,cycle = 0,0,1
flag = False
while True:
    for i in [0,1,0,1] + [0]*(cycle+1) + [1]*(cycle+1):
        if i == 0:
            bbun+=1
        else:
            degi+=1

        if (bbun if chant == '0' else degi) == T:
            flag = True
            break
    if flag:
        break
    cycle+=1

print((bbun+degi)%A - 1 if (bbun+degi)%A else (A-1))
