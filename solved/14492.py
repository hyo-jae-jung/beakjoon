from sys import stdin  

N = int(stdin.readline().strip())
A = []
B = []
for _ in range(N):
    A.append(list(map(int,stdin.readline().strip().split())))
    B.append([])
for _ in range(N):
    for i,j in enumerate(stdin.readline().strip().split()):
     B[i].append(int(j))

ans = 0
for i in A:
   for j in B:
      if sum(k*l for k,l in zip(i,j)) > 0:
         ans+=1

print(ans)
