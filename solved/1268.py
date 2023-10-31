from sys import stdin 

N = int(stdin.readline().strip())
arr = []
for _ in range(N):
    arr.append(list(map(int,stdin.readline().strip().split())))

    
ans = [set() for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i != j:
            for k in range(5):
                if arr[i][k] == arr[j][k]:
                    ans[i].add(j)

tmp = [len(i) for i in ans]
print(tmp.index(max(tmp))+1)
