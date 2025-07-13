from heapq import heappop,heappush

def next_permutation(arr):
    N = len(arr)
    h = []
    while len(arr) > 1:
        b = arr.pop()
        heappush(h,b)
        if arr[-1] < b:
            tmp = []
            c = arr.pop()
            while h:
                d = heappop(h)
                if c < d:
                    arr.append(d)
                    tmp.append(c)
                    c = N+1
                else:
                    tmp.append(d)
            return arr+tmp
    return [-1]

from sys import stdin  

ans = []
for i in stdin.read().strip().splitlines():
    s,n = i.split()
    d = {-1:'No permutation'}
    for j,k in enumerate(s,1):
        d.update({j:k})
    l = list(range(1,len(s)+1))
    for m in range(int(n)-1):
        l = next_permutation(l)
    t = ''
    for o in l:
        t+=d[o]
    ans.append(f"{s} {n} = {t}")

print(*ans,sep='\n')
