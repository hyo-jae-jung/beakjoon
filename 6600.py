from sys import stdin 

answer = []

def distance(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

while (tmp := stdin.readline().strip()):
    x1,y1,x2,y2,x3,y3 = map(float,tmp.split())
    answer.append(round(max(distance(x1,y1,x2,y2),distance(x3,y3,x2,y2),distance(x1,y1,x3,y3))*3.141592653589793,2))

print(*answer,sep='\n')
