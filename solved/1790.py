from sys import stdin  

N,k = map(int,stdin.readline().strip().split())

def a(n):
    return int(9*n*(10**(n-1)))

max_len = 0
m = 0
while 10**m <= N:
    max_len+=a(m)
    m+=1

max_len+=(N-(10**(m-1)-1))*m

if max_len >= k:
    s,i = 0,1
    while (s:=s+a(i)) < k:
        i+=1

    for j in range(1,i):
        k-=a(j)

    number = ((10**(i-1)-1) + k//i)

    if (l:=k%i) == 0:
        print(str(number)[-1])
    else:
        print(str(number+1)[l-1])
else:
    print(-1)
