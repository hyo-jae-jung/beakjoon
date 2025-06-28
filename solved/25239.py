from sys import stdin   

hh,mm = map(int,stdin.readline().strip().split(":"))
area = list(map(int,stdin.readline().strip().split()))
L = int(stdin.readline().strip())

def seal(hh):
    area[hh//2] = 0

def tick(h,m):
    global hh,mm
    tm = mm + m
    hh = (hh + h + tm//60)%12
    mm = tm%60

for _ in range(L):
    sT,act = stdin.readline().strip().split()
    s,T = map(int,sT.split("."))
    if s < 60 and sum(area) > 0:
        if act == '^':
            seal(hh)
        else:
            if act[1] == '0':
                tick(0,int(act[:2]))
            else:
                tick(int(act[0]),0)

print(min(sum(area),100))
