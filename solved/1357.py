from sys import stdin 

X,Y = stdin.readline().strip().split()

print(int(''.join(list(reversed(str(int(''.join(list(reversed(X))))+int(''.join(list(reversed(Y))))))))))
