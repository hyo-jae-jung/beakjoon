from sys import stdin 

n = int(stdin.readline().strip())

print(2**(n%2+n//2)%16769023)
