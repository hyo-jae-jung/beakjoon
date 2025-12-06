from sys import stdin   

N = int(stdin.readline().strip())

def f(n):
    return 9*n*(10**(n-1))

i = 1
while N > (t:=f(i)):
    N-=t
    i+=1

val = str(10**(i-1)-1 + (N//i) + (0 if N%i == 0 else 1))
print(val)
if N%i == 0:print(val[-1])
else:print(val[N%i-1])
