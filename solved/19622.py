from sys import stdin  

N = int(stdin.readline().strip())
K = [0]
for _ in range(N):
    _,_,cnt = map(int,stdin.readline().strip().split())
    K.append(cnt)

for i in range(3,N+1):
    K[i] += max(K[i-2],K[i-3])

print(max(K[-2:]))
