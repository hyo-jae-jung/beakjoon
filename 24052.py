from sys import stdin  

N,K = map(int,stdin.readline().strip().split())
A = list(map(int,stdin.readline().strip().split()))

for i in range(1,len(A)):
    target_val = A[i]
    check= False
    for j in range(i,0,-1):
        if target_val < A[j-1]:
            A[j] = A[j-1]
            print(A)
            check = True
        else:
            if check:
                A[j-1] = target_val
                print(A)
            break
    else:
        if check:
            A[j-1] = target_val
            print(A)
