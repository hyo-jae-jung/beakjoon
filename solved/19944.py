from sys import stdin 

N,M = map(int,stdin.readline().strip().split())
if M <= 2:
    print("NEWBIE!")
elif M <= N:
    print("OLDBIE!")
else:
    print("TLE!")
    