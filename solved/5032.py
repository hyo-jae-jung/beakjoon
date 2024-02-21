from sys import stdin 

e,f,c = map(int,stdin.readline().strip().split())
e+=f

ans = 0

while e >= c:
    tmp = e//c 
    ans+= tmp
    e = e%c + tmp

print(ans)
