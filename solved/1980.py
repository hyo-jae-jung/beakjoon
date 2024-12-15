import sys

n,m,t = map(int,sys.stdin.readline().strip().split())

n,m = min(n,m),max(n,m)

n_cnt,rest_t,m_cnt = t//n,t%n,0
rest_set = set(range(1,m-n+1))
if rest_t == 0:
    print(n_cnt,rest_t)
else:
    arr = [(n_cnt,rest_t)]
    while rest_set and n_cnt > 0:
        n_cnt-=1
        rest_t+=n
        if rest_t >= m:
            m_cnt+=1
            rest_t-=m
            if rest_t == 0:
                arr.append((n_cnt+m_cnt,rest_t))
                break
            else:
                rest_set.discard(rest_t)
                arr.append((n_cnt+m_cnt,rest_t))

    arr.sort(key=lambda x:(x[1],-x[0]))
    print(*arr[0])
