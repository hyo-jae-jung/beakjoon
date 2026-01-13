from sys import stdin 

N = int(stdin.readline().strip())

ans = 0
v = [True]*N
diagonal_a = [True]*(2*N-1)
diagonal_b = [True]*(2*N-1)

def solution(n=0):
    global N,ans,v,diagonal_a,diagonal_b
    if n == N:
        ans+=1
        return 

    for j in range(N):
        if v[j] and diagonal_a[j-n+(N-1)] and diagonal_b[j+n]:
            v[j] = False
            diagonal_a[j-n+(N-1)] = False
            diagonal_b[j+n] = False
            solution(n+1)
            v[j] = True
            diagonal_a[j-n+(N-1)] = True
            diagonal_b[j+n] = True 

solution()
print(ans)
