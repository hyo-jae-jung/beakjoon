from sys import stdin   

N,P = map(int,stdin.readline().strip().split())
d = {}
ans = 0
for _ in range(N):
    l_num,p_num = map(int,stdin.readline().strip().split())
    if not d.get(l_num):
        d.update({l_num:[0]})

    while d[l_num][-1] > p_num:
        d[l_num].pop()
        ans+=1

    if d[l_num][-1] < p_num:
        d[l_num].append(p_num)
        ans+=1

print(ans)
