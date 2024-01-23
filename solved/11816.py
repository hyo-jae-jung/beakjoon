from sys import stdin 

X = stdin.readline().strip()

if X[0] == '0':
    if X[1] == 'x':
        print(int(X[2:],16))
    else:
        print(int(X[1:],8))
else:
    print(X)
