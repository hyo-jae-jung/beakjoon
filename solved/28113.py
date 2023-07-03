from sys import stdin 

N,A,B = map(int,stdin.readline().strip().split())
if A < B:
    print('Bus')
elif A > B:
    print('Subway')
else:
    print('Anything')
    