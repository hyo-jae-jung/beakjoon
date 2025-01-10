from sys import stdin  

N,K = map(int,stdin.readline().strip().split())
A = list(map(int,stdin.readline().strip().split()))

def main():

    swap_cnt = 0
    for i in range(len(A)-1,-1,-1):
        max_idx = i
        for j in range(i-1,-1,-1):
            if A[max_idx] < A[j]:
                max_idx = j

        if i != max_idx:
            swap_cnt+=1
            A[max_idx],A[i] = A[i],A[max_idx]
        if K == swap_cnt:
            return sorted([A[max_idx],A[i]])

    return [-1]

print(*main())
