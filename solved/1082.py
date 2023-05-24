from sys import stdin 

N = int(stdin.readline().strip())
P_i = [(i,int(j)) for i,j in enumerate(stdin.readline().strip().split())]
M = int(stdin.readline().strip())

P_p = sorted(P_i,key=lambda x:-x[1])

level_v = P_p.pop()
idx_by_small_value = level_v[1]
level = M//idx_by_small_value

rest = M - level*idx_by_small_value
l = [level_v[0]]*level

i = level-1

while i > -1:
    for j in range(N-1,0,-1):
        if rest >= P_i[j][1] - idx_by_small_value:
            l[i] = P_i[j][0]
            rest-=P_i[j][1]
            rest+=idx_by_small_value
            break
    else:
        if l[-1] == 0 and len(l) > 1:
            l.pop()
            rest+=idx_by_small_value
    i-=1

print(''.join(str(i)for i in reversed(l)))
