from sys import stdin   

_,_,_ = stdin.readline().strip().split()
A = set(stdin.readline().strip().split())
B = set(stdin.readline().strip().split())
G = list(stdin.readline().strip().split())

a,b = 0,0

for i in G:
    if i in A:
        a+=1
    elif i in B:
        b+=1

if a > b:
    print('A')
elif a < b:
    print('B')
else:
    print('TIE')
