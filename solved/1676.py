import sys

N = int(sys.stdin.readline().strip())
answer = eval('*'.join(map(str,list(range(1,N+1) if N != 0 else range(0,1)))))

cnt=0
while True:
    if answer == 0 or answer%10**(cnt+1) != 0:
        break
    else:
        cnt+=1

print(cnt)

