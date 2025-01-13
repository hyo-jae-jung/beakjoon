from sys import stdin  

x = int(stdin.readline().strip())

if x%3 == 1:
    print('U')
elif x%3 == 2:
    print('O')
else:
    print('S')
    