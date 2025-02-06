from sys import stdin   

N,A,B = map(int,stdin.readline().strip().split())

a,b = 1,1

for _ in range(N):
    a+=A
    b+=B

    if a < b:
        a,b = b,a
    elif a == b:
        b-=1
    
print(a,b)
