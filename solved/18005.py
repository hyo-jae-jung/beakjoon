from sys import stdin  

n = int(stdin.readline().strip())

if n%2 == 1:
    print(0)
else:
    if (n//2)%2 == 1:
        print(1)
    else:
        print(2)
        
