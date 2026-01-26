from sys import stdin  

N,M = map(int,stdin.readline().strip().split())
trains = [0]*N
for _ in range(M):
    tmp = list(map(int,stdin.readline().strip().split()))
    if tmp[0] == 1:
        trains[tmp[1]-1] |= (1 << (tmp[2]-1))
    elif tmp[0] == 2:
        tmp_val = (1 << (tmp[2]-1))
        if trains[tmp[1]-1] & tmp_val == tmp_val:
            trains[tmp[1]-1]-=tmp_val
    elif tmp[0] == 3:
        trains[tmp[1]-1]<<=1
        trains[tmp[1]-1]&=((1 << 20)-1)
    elif tmp[0] == 4:
        trains[tmp[1]-1]>>=1

ans = set()
for train in trains:
    if train not in ans:
        ans.add(train)

print(len(ans))
