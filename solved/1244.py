from sys import stdin  

N = int(stdin.readline().strip())
switch = list(map(int,stdin.readline().strip().split()))
M = int(stdin.readline().strip())

def man(idx):
    for i in range(idx-1,N,idx):
        if switch[i]:switch[i] = 0
        else:switch[i] = 1

def woman(idx):
    idx-=1
    i = 0
    while idx-i >= 0 and idx+i < N:
        if switch[idx-i] == switch[idx+i]:
            if switch[idx-i]:
                switch[idx-i] = 0
                switch[idx+i] = 0
            else:
                switch[idx-i] = 1
                switch[idx+i] = 1
        else:
            return
        i+=1

for _ in range(M):
    a,b = map(int,stdin.readline().strip().split())
    if a == 1:
        man(b)
    else:
        woman(b)

tmp = []
for i,j in enumerate(switch):
    if i%20 == 0:
        if tmp:
            print(*tmp)
        tmp = [j]
    else:
        tmp.append(j)
else:
    if tmp:
        print(*tmp)
