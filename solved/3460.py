from sys import stdin 

T = int(stdin.readline().strip())

ans = []
for _ in range(T):
    tmp = []
    for i,j in enumerate(reversed(bin(int(stdin.readline().strip()))[2:])):
        if j == '1':
            tmp.append(i)
    ans.append(tmp)

for i in ans:
    print(*i)
