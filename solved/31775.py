from sys import stdin  

a = stdin.readline().strip()
b = stdin.readline().strip()
c = stdin.readline().strip()

tmp = set([a[0],b[0],c[0]])

if len(tmp) == 3 and set(['l','k','p']) == tmp:
    print("GLOBAL")
else:
    print("PONIX")
    