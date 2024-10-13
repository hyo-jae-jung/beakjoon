from sys import stdin  

ans = 0

m = {}
for i in range(15):
    m.update({chr(i+65):(i//4,i%4)})

arr = []
for _ in range(4):
    arr.append(list(stdin.readline().strip()))

for i in range(4):
    for j in range(4):
        if arr[i][j] != '.':
            ans+=abs(m[arr[i][j]][0] - i)
            ans+=abs(m[arr[i][j]][1] - j)

print(ans)
