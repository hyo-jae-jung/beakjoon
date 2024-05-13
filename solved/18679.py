from sys import stdin 

N = int(stdin.readline().strip())
m = {}
for _ in range(N):
    i,_,o = stdin.readline().strip().split()
    m.update({i:o})
ans = []
T = int(stdin.readline().strip())
for _ in range(T):
    K = int(stdin.readline().strip())
    tmp = stdin.readline().strip().split()
    decode = []
    for i in tmp:
        decode.append(m[i])
    ans.append(' '.join(decode))

print(*ans,sep='\n')
