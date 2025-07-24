from sys import stdin  

N = int(stdin.readline().strip())
arr = []
for _ in range(N):
    arr.append(stdin.readline().strip())

cost = {}
for i,j in zip(['P','C','V','S','G','F'],map(int,stdin.readline().strip().split())):
    cost.update({i:j})

O = int(stdin.readline().strip())
cost.update({'O':O})

ans = 0

for i in range(N):

    l = len(arr[i])
    if arr[i][0] == 'O':
        ans+=cost['O']*l
        continue

    for j in range(1,l):
        if arr[i][0] != arr[i][j]:
            ans+=cost['O']*l
            break
    else:
        ans+=l*(cost[arr[i][0]] if cost[arr[i][0]] < cost['O'] else cost['O'])

print(ans)
