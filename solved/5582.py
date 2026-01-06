from sys import stdin  

A = '0' + stdin.readline().strip()
B = '9'+ stdin.readline().strip()

la = len(A)
lb = len(B)
ans = 0

def solution(x,y):
    global A,B,la,lb
    d = 1
    while 0 <= (nx:=x+d) < la and 0 <= (ny:=y+d) < lb and A[nx] == B[ny]:
        d+=1
    return d

for i in range(1,lb):
    for j in range(1,la):
        if A[j-1] != B[i-1] and A[j] == B[i]:
            ans = max(ans,solution(j,i))

print(ans)
