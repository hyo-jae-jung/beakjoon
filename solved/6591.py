from sys import stdin  

def comb_fast(n, k):
    if k > n - k:
        k = n - k
    res = 1
    for i in range(1, k+1):
        res = res * (n - i + 1) // i
    return res

ans = []
while (s:=stdin.readline().strip()) != '0 0':
    n,k = map(int,s.split())
    ans.append(comb_fast(n,k))

print(*ans,sep='\n')
