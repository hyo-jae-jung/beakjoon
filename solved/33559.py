from sys import stdin  

N = int(stdin.readline().strip())
A = list(map(int,stdin.readline().strip().split()))
B = list(map(int,stdin.readline().strip().split()))

A.sort()
B.sort()

A_o,B_o = [],[]
A_x,B_x = [],[]

while A and B:
    if A[-1] == B[-1]:
        A_o.append(A.pop())
        B_o.append(B.pop())
        continue

    if A[-1] > B[-1]:
        A_x.append(A.pop())
        continue

    if A[-1] < B[-1]:
        B_x.append(B.pop())
        continue

print(len(A_o))
print(*(A_o+A+A_x))
print(*(B_o+B+B_x))
