from sys import stdin  

N,K = map(int,stdin.readline().strip().split())
A = list(map(int,stdin.readline().strip().split()))

save = []

for i in range(1,len(A)):
    save_tmp = []
    check = False
    start_val = A[i]
    for j in range(i,0,-1):
        if A[j] < A[j-1]:
            A[j],A[j-1] = A[j-1],A[j]
            save_tmp.append(A[j])
            check = True
        else:
            if check:
                save_tmp.append(start_val)
            break
    else:
        if check:
            save_tmp.append(start_val)
    save.extend(save_tmp)

if len(save) >= K:
    print(save[K-1])
else:
    print(-1)
