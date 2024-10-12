from sys import stdin  

N = int(stdin.readline().strip())
A = list(map(int,stdin.readline().strip().split()))

ans = 'NO'
switch = True 

for i in range(1,N):

    if A[i] == A[i-1]:
        break

    if switch:
        if A[i] < A[i-1]:
            switch = False
    else:
        if A[i] > A[i-1]:
            break
else:
    ans = 'YES'
    
print(ans)
