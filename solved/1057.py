from sys import stdin 

N,kim,im = map(int,stdin.readline().strip().split())

def round(x:int)->int:
    return int(x/2) if x%2==0 else int((x+1)/2)

a = min(kim,im)
b = max(kim,im)

cnt=1
while abs(a-b) > 1 or a%2==0:
    a = round(a)
    b = round(b)
    cnt+=1

print(cnt)

