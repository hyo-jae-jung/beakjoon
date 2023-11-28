from sys import stdin 

N = int(stdin.readline().strip())

ans = 0

i = 1
while N:
    if i*(i+1)//2 > N:
        N-=i*(i-1)//2
        ans+=i-1
        i=1
    else:
        i+=1

print(ans)
