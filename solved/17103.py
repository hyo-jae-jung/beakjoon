from sys import stdin 

T = int(stdin.readline().strip())
test_cases = []
max_t = 0
for _ in range(T):
    t = int(stdin.readline().strip())
    max_t = t if t > max_t else max_t
    test_cases.append(t)

def sieve_of_eratosthenes(n):
    sieve = [False]*2 + [True]*(n-1)
    m = int(n**0.5)
    for i in range(2,m+1):
        if sieve[i]:
            for j in range(i+i,n+1,i):
                sieve[j] = False
                
    return sieve

sieve = sieve_of_eratosthenes(max_t)

for i in test_cases:
    cnt = 0
    multi_check = [True]*(i+1)
    for k in (j for j in range(2,i+1) if sieve[j]):
        if multi_check[k]:
            diff = i-k
            cnt+=sieve[diff]
            multi_check[diff] = False
            
    print(cnt)
    