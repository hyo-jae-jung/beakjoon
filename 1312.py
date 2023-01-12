from sys import stdin 
from math import log10

A,B,N = map(int,stdin.readline().strip().split())
temp = ''
exec('\'{:.'+str(N+1)+'f}\''+'.format(A/B)')

print(temp)
