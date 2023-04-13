from sys import stdin 

N = int(stdin.readline().strip())
A = map(int,stdin.readline().strip().split())

one = N
two = N-1
three = 1
answer = []
for i,j in zip(A,range(N,0,-1)):
    if i == 1:
        answer.append((one,j))
        if one == two+1:
            one-=1
            two-=1
        else:
            one = two+1
    elif i == 2:
        answer.append((two,j))
        two-=1
    else:
        answer.append((three,j))
        three+=1
        
print(*[j for _,j in sorted(answer,key=lambda x:-x[0])])
