from sys import stdin  

S = list(stdin.readline().strip())
T = list(stdin.readline().strip())

ans = 0

while T:
    if (tmp:=T.pop()) == 'B':
        tmp_T = []
        while T:
            tmp_T.append(T.pop())
        T = tmp_T

    if T == S:
        ans = 1
        break

print(ans)
