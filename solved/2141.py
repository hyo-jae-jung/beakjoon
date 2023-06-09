from sys import stdin

N = int(stdin.readline().strip())
XA = []
for _ in range(N):
    XA.append(tuple(map(int,stdin.readline().strip().split())))

XA.sort(key=lambda x:x[0])

A = []
for _,i in XA:
    A.append(i)

left = 0
right = sum(A)
diff = abs(right-left)
temp = 0
i = 0

while i<N:
    right-=A[i]
    temp = abs(right-left)
    if diff > temp:
        diff = temp
        left+=A[i]
        i+=1
    else:
        break

print(XA[i-1][0])
