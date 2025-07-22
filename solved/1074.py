import sys 
sys.setrecursionlimit(10**7)

N,r,c = map(int,sys.stdin.readline().strip().split())

def recursion(n,v=0,i=0,j=0):

    global r,c
    if i == c and j == r:
        return v

    t = 2**(n-1)

    if i <= c < i+t and j <= r < j+t:
        return recursion(n-1,v,i,j)

    if i+t <= c < i+2*t and j <= r < j+t:
        return recursion(n-1,v+t**2,i+t,j)
    
    if i <= c < i+t and j+t <= r < j+2*t:
        return recursion(n-1,v+2*t**2,i,j+t)

    if i+t <= c < i+2*t and j+t <= r < j+2*t:
        return recursion(n-1,v+3*t**2,i+t,j+t)
    
print(recursion(N))
