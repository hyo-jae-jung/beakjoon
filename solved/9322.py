from sys import stdin  

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    n = int(stdin.readline().strip())
    key_1 = list(stdin.readline().strip().split())
    key_2 = list(stdin.readline().strip().split())
    encrypt_text = list(stdin.readline().strip().split())
    algorithm = []

    for i in key_1:
        for j in range(n):
            if i == key_2[j]:
                algorithm.append(j)
                break
    tmp = []
    for i in algorithm:
        tmp.append(encrypt_text[i])

    ans.append(tmp)

for i in ans:
    print(*i)
