from sys import stdin   

N = int(stdin.readline().strip())
A = list(map(int,stdin.readline().strip().split()))

if N <= max(A):
    print(N)
else:
    A.sort(reverse=True)
    effect = 0
    for i in range(N):
        if A[i] != 0:
            effect = max(effect,i + A[i])
        else:
            break

    print(effect if effect <= N else N)
