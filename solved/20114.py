from sys import stdin  

N,H,W = map(int,stdin.readline().strip().split())
note = []
for _ in range(H):
    note.append(list(stdin.readline().strip()))

ans = ''

def solution(note,h,w):
    for j in range(i*w,(i+1)*w):
            for k in range(h):
                if note[k][j] != '?':
                    return note[k][j]
    return '?'

for i in range(N):
    ans+=solution(note,H,W)

print(ans)
