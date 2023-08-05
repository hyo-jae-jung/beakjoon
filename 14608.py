from sys import stdin 

K = int(stdin.readline().strip())
C = list(map(int,stdin.readline().strip().split()))
a,b,N = map(int,stdin.readline().strip().split())
dx = (b-a)/N
n = b-a
integeral = ((b**n)-(a**n))/(n)

print((integeral-a)/(dx**))

