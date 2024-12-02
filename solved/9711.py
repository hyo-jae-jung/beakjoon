import sys
sys.setrecursionlimit(10**6)

T = int(sys.stdin.readline().strip())
ans = []
memo = {1:1,2:1}

def fibonacci(n):

    if memo.get(n):
        return memo.get(n)

    if n == 1:
        return 1
    
    if n == 2:
        return 1
    
    memo.update({n:fibonacci(n-1) + fibonacci(n-2)})

    return memo[n]

for _ in range(T):
    P,Q = map(int,sys.stdin.readline().strip().split())
    ans.append(fibonacci(P)%Q)

for i,j in enumerate(ans,1):
    print(f"Case #{i}: {j}")
