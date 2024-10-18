from sys import stdin  

R,C = map(int,stdin.readline().strip().split())
arr = []
for _ in range(R):
    arr.append(list(stdin.readline().strip()))
ans = [0]*5

for i in range(R-1):
    for j in range(C-1):
        if arr[i][j] == '#' or arr[i+1][j] == '#' or arr[i][j+1] == '#' or arr[i+1][j+1] == '#':
            continue
        else:
            cnt = 0
            for k in range(i,i+2):
                for l in range(j,j+2):
                    if arr[k][l] == 'X':
                        cnt+=1

        ans[cnt]+=1

for i in ans:
    print(i)
    