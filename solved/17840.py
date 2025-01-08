from sys import stdin  

Q,M = map(int,stdin.readline().strip().split())

def find_pisano_period(m):
    ans = [0,1]
    while ans[:len(ans)//2] != ans[len(ans)//2:]:
        for _ in range(2):
            ans.append((ans[-1]+ans[-2])%m)
    
    return ans[:len(ans)//2]

pisano_period = find_pisano_period(M)
new_s = ''.join(map(str,pisano_period))

ans = []

for _ in range(Q):
    ans.append(new_s[int(stdin.readline().strip())%len(new_s)])

print(*ans,sep='\n')
