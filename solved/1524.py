from sys import stdin 

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    _ = stdin.readline()
    N,M = map(int,stdin.readline().strip().split())
    S = list(map(int,stdin.readline().strip().split()))
    B = list(map(int,stdin.readline().strip().split()))
    
    S.sort(reverse=True)
    B.sort(reverse=True)

    while S and B:
        if S[-1] < B[-1]:
            S.pop()
        else:
            B.pop()

    ans.append('B' if B else 'S')
        
print(*ans,sep='\n')
