from sys import stdin 

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    ans_tmp = []
    N = int(stdin.readline().strip())
    memo1 = set(map(int,stdin.readline().strip().split()))
    M = int(stdin.readline().strip())
    memo2 = list(map(int,stdin.readline().strip().split()))

    for i in memo2:
        if i in memo1:
            ans_tmp.append(1)
        else:
            ans_tmp.append(0)
    ans.append(ans_tmp)

for i in ans:
    print(*i,sep='\n')
    