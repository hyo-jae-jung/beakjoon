from sys import stdin  

n = int(stdin.readline().strip())
music = []
for _ in range(n):
    music.append(int(stdin.readline().strip()))

abcdef = {'A':0,'B':2,'C':3,'D':5,'E':7,'F':8,'G':10,0:'A',2:'B',3:'C',5:'D',7:'E',8:'F',10:'G'}
ans = []
for alphabet in map(chr,range(65,65+7)):
    loc = abcdef[alphabet]
    for d in music:
        if not (loc:=abcdef.get((loc+d)%12)):
            break
        loc = abcdef[loc]
    else:
        ans.append(f"{alphabet} {abcdef[loc]}")

print(*ans,sep='\n')
