from sys import stdin 

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    J,N = map(int,stdin.readline().strip().split())
    space = []
    for _ in range(N):
        R,C = map(int,stdin.readline().strip().split())
        space.append(R*C)
    space.sort(reverse=True)

    I=0
    for i in space:
        print(1111,I,i,J)
        if J >= i:
            J-=i
            I+=1
        else:
            I+=1
            ans.append(I)
            break

print(*ans,sep='\n')
