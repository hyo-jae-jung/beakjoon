from sys import stdin 

W,H,K = map(int,stdin.readline().strip().split())
N = int(stdin.readline().strip())
Y = list(map(int,stdin.readline().strip().split()))
M = int(stdin.readline().strip())
X = list(map(int,stdin.readline().strip().split()))

NY = [Y[0]]
for i in range(1,N):
    if (tmp:=Y[i]-Y[i-1]) <= K:
        NY.append(tmp)
else:
    if (tmp:=H-Y[-1]) <= K:
        NY.append(tmp)
NY.sort()

NX = [X[0]]
for i in range(1,M):
    if (tmp:=X[i]-X[i-1]) <= K:
        NX.append(tmp)
else:
    if (tmp:=W-X[-1]) <= K:
        NX.append(tmp)
NX.sort()

def solution(x):
    left = 0
    right = len(NY)-1
    while left < right:
        mid = (left+right)//2
        if NY[mid]*x <= K:
            left = mid + 1
        else:
            right = mid
    return right

ans = 0
for x in NX:
    tmp_idx = solution(x)
    ans+=tmp_idx + (1 if NY[tmp_idx]*x <= K else 0)

print(ans)
