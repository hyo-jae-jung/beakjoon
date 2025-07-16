from sys import stdin  

N,K = map(int,stdin.readline().strip().split())
distance = []
for _ in range(N):
    pn = int(stdin.readline().strip())
    p = list(map(int,stdin.readline().strip().split()))
    P = []
    for i in range(0,2*pn,2):
        t = []
        for j in range(i,i+2):
            t.append(p[j])
        P.append(t)
    
    max_d = 0
    for i,j in P:
        max_d = max(i**2+j**2,max_d)

    distance.append(max_d)

print(f"{sorted(distance)[K-1]:.2f}")
