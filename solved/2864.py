from sys import stdin 

A,B = stdin.readline().strip().split()

min = 0
delta = 0

def cal(num:str):
    global min, delta
    for i,j in zip(range(len(num)-1,-2,-1),num):
        if int(j) in [5,6]:
            delta+=(10**i)
            min+=5*(10**i)
        else:
            min+=int(j)*(10**i)
    
cal(A)
cal(B)
print(min,min+delta)
