from sys import stdin  

N = int(stdin.readline().strip())
A = list(map(int,stdin.readline().strip().split()))
B = list(map(int,stdin.readline().strip().split()))

def main(N,A,B):
    
    for i in range(1,N):
        if A[i] < A[i-1]:
            target = A[i]
            A[i] = A[i-1]

            if A == B:
                return 1
            
            for j in range(i-1,0,-1):
                if target < A[j-1]:
                    A[j] = A[j-1]
        
                    if A == B:
                        return 1
                else:
                    A[j] = target
        
                    if A == B:
                        return 1
                    break
            else:
                A[0] = target
    
                if A == B:
                    return 1
    else:
        return 0
    
print(main(N,A,B))
