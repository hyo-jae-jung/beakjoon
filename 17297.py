from sys import stdin  

N = int(stdin.readline().strip())

def messi(n):

    if n == 1:
        return "Messi"
    
    if n == 2:
        return "Messi Gimossi"
    
    return  messi(n-1) + " " + messi(n-2)

print(messi(N))
