from sys import stdin 

T = int(stdin.readline().strip())
ans = []
for i in range(1,T+1):
    W = stdin.readline().strip()
    w_len = len(W)
    result = 1
    for j in range(w_len):
        s = set()
        for k in [-1,0,1]:
            if 0 <= (jk:=j+k) < w_len:
                s.add(W[jk])
        result*=len(s)%(10**9+7)
    ans.append(f"Case #{i}: {result%(10**9+7)}")

print(*ans,sep='\n')
