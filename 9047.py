from sys import stdin 

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    tmp = stdin.readline().strip()
    cnt = 0
    while tmp != '6174':
        tmp = str(int(''.join(sorted(list(tmp),reverse=True))) - int(''.join(sorted(list(tmp)))))
        cnt+=1
    ans.append(cnt)

print(*ans,sep='\n')
