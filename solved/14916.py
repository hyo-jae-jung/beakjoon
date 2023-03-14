from sys import stdin 

n = int(stdin.readline().strip())

def charge_cnt(n):
    if n//5 == 0 and n in [1,3]:
        return -1
    
    return n//5 + ((n%5)//2 if (n%5)%2 == 0 else (n%5+5)//2 - 1)
    
print(charge_cnt(n))
