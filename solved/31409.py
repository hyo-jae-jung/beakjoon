from sys import stdin  

N = int(stdin.readline().strip())
A = [0] + list(map(int,stdin.readline().strip().split()))

cnt = 0
for i in range(1,N+1):
    if i == A[i]:
        A[i] = (i+1)%N if (i+1)%N > 0 else N
        cnt+=1

print(cnt)
print(*A[1:])
