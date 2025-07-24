from sys import stdin   
from collections import deque

N = int(stdin.readline().strip())
S = list(map(int,stdin.readline().strip().split()))

max_cnt = 0
q = deque()
s = set()

for i,j in enumerate(S):
    if not q:
        q.append(i)
        s.add(j)
        continue

    if S[q[-1]] != j:
        if len(q) == 1:
            q.append(i)
            s.add(j)
        else:
            if j in s:
                q[-1] = i
            else:
                p = q.popleft()
                max_cnt = max(max_cnt,i - p)
                s = set([S[q[0]]])
                q.append(i)
                s.add(j)
else:
    max_cnt = max(max_cnt, N - q[0])

print(max_cnt)
