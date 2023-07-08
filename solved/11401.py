from sys import stdin 

N,K = map(int,stdin.readline().strip().split())
p = 10**9+7

def f(n,p):
    answer = 1
    for i in range(2,n+1):
        answer*=i
        answer%=p
    return answer

def div_conquer(n,d,p):
    if d == 1:
        return n%p

    if d%2:
        return (div_conquer(n,d//2,p)**2)*n % p
    else:
        return (div_conquer(n,d//2,p)**2) % p

print(((f(N,p)%p)*div_conquer(f(K,p)*f(N-K,p),p-2,p))%p)
