from sys import stdin  

N = int(stdin.readline().strip())
A,B = 2,1
ans = 0

while A > B:
    tmp = A**2 - B**2
    if tmp < N:
        A+=1
    elif tmp > N:
        B+=1
    else:
        ans+=1
        A+=1

print(ans)
