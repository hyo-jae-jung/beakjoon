from sys import stdin  

a,b,c = map(int,stdin.readline().strip().split())
N = int(stdin.readline().strip())
arr = [2]*(1+a+b+c)
items = []
for _ in range(N):
    i,j,k,r = map(int,stdin.readline().strip().split())
    if r == 0:
        items.append((i,j,k))
    else:
        arr[i] = 1
        arr[j] = 1
        arr[k] = 1

for i,j,k in items:
    if arr[i] + arr[j] + arr[k] == 4 and 1 in (arr[i],arr[j],arr[k]):
        for l in [i,j,k]:
            if arr[l] == 2:
                arr[l] = 0
                break

print(*arr[1:],sep='\n')
