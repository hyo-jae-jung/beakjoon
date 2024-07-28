from sys import stdin 

a = 0
for i in range(3,0,-1):
    a+=i*int(stdin.readline().strip())

b = 0
for i in range(3,0,-1):
    b+=i*int(stdin.readline().strip())

if a > b:
    print('A')
elif a < b:
    print('B')
else:
    print('T')
    