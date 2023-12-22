from sys import stdin 

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    N = stdin.readline().strip()
    tmp = str(int(N) + int(''.join(list(reversed(N)))))
    for i in range(len(tmp)//2+len(tmp)%2):
        if tmp[i] != tmp[-(i+1)]:
            ans.append('NO')
            break
    else:
        ans.append('YES')

print(*ans, sep='\n')
