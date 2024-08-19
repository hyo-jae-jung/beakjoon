from sys import stdin  

A,B = map(int,stdin.readline().strip().split())
ans = []
b=A-1
a=B+1
if B>=b:
    ans.append(A+b)
elif A>=a:
    ans.append(a+B)

print(max(ans))
