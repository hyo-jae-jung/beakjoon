import sys

N = int(sys.stdin.readline().strip())
N_list = sorted(list(map(int,sys.stdin.readline().strip().split())))
M = int(sys.stdin.readline().strip())
M_list = list(map(int,sys.stdin.readline().strip().split()))

d = dict.fromkeys(M_list,0)

n = 0
while N_list:
    val = N_list[0]
    try:
        if N_list[n] != N_list[n+1]:
            cnt = len(N_list[:n+1])
            d[val]+=cnt
            N_list = N_list[cnt:]
            n = 0
        else:
            n+=1
    except KeyError:
        N_list = N_list[cnt:]
        n = 0
    except IndexError:
        cnt = len(N_list)
        d[val]+=cnt
        break

print(*d.values())
