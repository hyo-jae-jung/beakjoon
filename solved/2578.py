from sys import stdin  

table = [list(map(int,stdin.readline().strip().split())) for _ in range(5)]

call = []
for _ in range(5):
    call+=list(map(int,stdin.readline().strip().split()))

cnt = 0
l,r = 0,0
def check_bingo(i,j):
    global cnt,l,r
    if sum(table[i]) == 0:
        cnt+=1

    tmp = 0
    for k in range(5):
        if table[k][j] > 0:
            tmp+=1
            break
    else:
        if tmp == 0:
            cnt+=1
    
    if r == 0 and i == j:
        rr = 0
        for k in range(5):
            if table[k][k] > 0:
                rr+=1
                break
        if rr == 0:
            r+=1

    if l == 0 and i+j == 4:
        ll = 0
        for k in range(5):
            if table[k][4-k] > 0:
                ll+=1
                break
        if ll == 0:
            l+=1

def find_num(n):
    for i in range(5):
        for j in range(5):
            if table[i][j] == n:
                return (i,j)
            
ans = 0
for i in call:
    a,b = find_num(i)
    table[a][b] = 0
    check_bingo(a,b)
    ans+=1
    if cnt + r + l > 2:
        print(ans)
        break
