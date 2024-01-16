from sys import stdin 
N,M = map(int,stdin.readline().strip().split())
a = []
for _ in range(N):
    a.append(list(stdin.readline().strip()))

aa = []
for _ in range(N):
    aa.append(list(stdin.readline().strip()))

def solusion():
    for i in range(N):
        for j in range(M):
            if (a[i][j] != aa[i][2*j]) or (a[i][j] != aa[i][2*j+1]):
                return 'Not Eyfa'
    return 'Eyfa'        
        
print(solusion())
