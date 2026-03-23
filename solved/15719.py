from sys import stdin 

N = int(stdin.readline().strip())
A = stdin.readline().strip() + ' '
ba = bytearray(N+1)
a,b = 0,1
while b < len(A):
    if A[b] == ' ':
        if ba[int(A[a:b])] == 0:
            ba[int(A[a:b])] = 1
            a,b = b+1,b+2
        else:
            print(A[a:b])
            break
    else:
        b+=1
