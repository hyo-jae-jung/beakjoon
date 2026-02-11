from sys import stdin  

N = int(stdin.readline().strip())
A = list(map(int,stdin.readline().strip().split()))
X = int(stdin.readline().strip())
A[A.index(-1)] = X

A.sort()

def postorder(arr):
    if len(arr) == 1:
        return arr
    
    d = len(arr)//2
    left = arr[:d].copy()
    right = arr[d+1:].copy()

    return postorder(left) + postorder(right) + [arr[d]]

print(*postorder(A))
