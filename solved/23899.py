from sys import stdin  

N = int(stdin.readline().strip())
A = list(map(int,stdin.readline().strip().split()))
C = list(map(int,stdin.readline().strip().split()))

def main():

    if A == C:
        return 1

    global N
    d = {}
    for i in range(len(A)):
        d.update({A[i]:i})

    B = A.copy()
    
    B.sort()
    swap_cnt = 0
    for i in range(len(A)-1,-1,-1):

        max_idx = d[B[i]]

        if i != max_idx:
            swap_cnt+=1
            d[A[max_idx]] = i
            d[A[i]] = max_idx
            A[max_idx],A[i] = A[i],A[max_idx]

        if A == C:
            return 1
        
    return 0

print(main())
