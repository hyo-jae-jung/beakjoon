from sys import stdin  

A = list(map(int,stdin.readline().strip().split()))
B = list(map(int,stdin.readline().strip().split()))

for i in range(10):
    if A[i] > B[i]:
        A[i] = 3
        B[i] = 0
    elif A[i] < B[i]:
        A[i] = 0
        B[i] = 3
    else:
        A[i] = 1
        B[i] = 1

print(aa:=sum(A),bb:=sum(B))
if aa > bb:
    print('A')
elif aa < bb:
    print('B')
else:
    while A and B:
        a = A.pop()
        b = B.pop()
        if a > b:
            print('A')
            break
        elif a < b:
            print('B')
            break
    else:
        print('D')
