import sys
n,m =map(int,sys.stdin.readline().strip().split())

up = int(eval('*'.join(map(str,range(m+1,n+1))) + '/('+'*'.join(map(str,range(1,n-m+1))) + ')'))
cnt=0
while up%10**(cnt+1) == 0:
    cnt+=1
print(cnt)
