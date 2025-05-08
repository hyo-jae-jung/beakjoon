from sys import stdin  

while (t:=stdin.readline().strip()) != '0 0':
    a,b = map(int,t.split())
    a,b = min(a,b),max(a,b)
    diff = b - a
    print(a - diff)
    