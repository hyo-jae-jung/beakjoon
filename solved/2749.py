from sys import stdin 

n = int(stdin.readline().strip())

a,b = 0,1
for _ in range(n%(15*10**5)-1):
    a,b = b%1000000,(a+b)%1000000
    
print(b)
