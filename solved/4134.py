from sys import stdin 

T = int(stdin.readline().strip())
ns = []
for _ in range(T):
    ns.append(int(stdin.readline().strip()))

def find_prime(n):
    if n in [0,1,2]:
        return 2
    
    m = int(n**0.5)+1
    while True:
        for i in range(2,m+1):
            if n%i == 0:
                break
        else:
            break
        n+=1
    return n

for i in ns:
    print(find_prime(i))
