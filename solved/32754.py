def solution(R,x1,y1,x2,y2,x3,y3,x4,y4):
    mx = (x1+x2+x3+x4)/4
    my = (y1+y2+y3+y4)/4
    if ((mx-x1)**2+(my-y1)**2)**0.5 + R >= (mx**2+my**2)**0.5:
        return 1
    return 0

from sys import stdin  

N,R = map(int,stdin.readline().strip().split())
ans = 0
for _ in range(N):
    ans+=solution(R,*map(int,stdin.readline().strip().split()))

print(ans)
