import sys
n,m =map(int,sys.stdin.readline().strip().split())

u = set(range(m+1,n+1))
d = set(range(1,n-m+1))

A = u-d
B = d-u

a = 1
for i in A:
    a*=i
b = 1
for i in B:
    b*=i

up = int(a/b)
cnt=0
while up%10**(cnt+1) == 0:
    cnt+=1
print(cnt)




# up = int(eval('*'.join(map(str,range(m+1,n+1))) + '/('+'*'.join(map(str,range(1,n-m+1))) + ')'))
