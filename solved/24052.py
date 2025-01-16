from sys import stdin  

N,K = map(int,stdin.readline().strip().split())
A = list(map(int,stdin.readline().strip().split()))

def main(N,K,A):
    cnt = 0
    for i in range(1,N):
        if A[i] < A[i-1]:
            target = A[i]
            A[i] = A[i-1]
            cnt+=1
            if cnt == K:
                return A
            
            for j in range(i-1,0,-1):
                if target < A[j-1]:
                    A[j] = A[j-1]
                    cnt+=1
                    if cnt == K:
                        return A
                else:
                    A[j] = target
                    cnt+=1
                    if cnt == K:
                        return A
                    break
            else:
                A[0] = target
                cnt+=1
                if cnt == K:
                    return A
    else:
        return [-1]
    
print(*main(N,K,A))
