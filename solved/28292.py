from sys import stdin   

N = int(stdin.readline().strip())

if N < 3:
    print(1)
elif 3 <= N < 6:
    print(2)
else:
    print(3)
