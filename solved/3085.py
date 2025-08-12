from sys import stdin   

N = int(stdin.readline().strip())
candies = [list(stdin.readline().strip()) for _ in range(N)]

def check_col(arr,x,y):
    sd_val = arr[y][x]

    dx = -1
    l_cnt = 0
    while x+dx >= 0:
        if sd_val == arr[y][x+dx]:
            l_cnt+=1
        else:
            break
        dx-=1

    dx = 1
    r_cnt = 0
    while x+dx < N:
        if sd_val == arr[y][x+dx]:
            r_cnt+=1
        else:
            break
        dx+=1
    return l_cnt + 1 + r_cnt

def check_row(arr,x,y):
    sd_val = arr[y][x]

    dy = -1
    u_cnt = 0
    while y+dy >= 0:
        if sd_val == arr[y+dy][x]:
            u_cnt+=1
        else:
            break
        dy-=1

    dy = 1
    d_cnt = 0
    while y+dy < N:
        if sd_val == arr[y+dy][x]:
            d_cnt+=1
        else:
            break
        dy+=1
    return u_cnt + 1 + d_cnt

ans = 0
for i in range(N):
    for j in range(N):
        if j > 0:
            candies[i][j-1],candies[i][j] = candies[i][j],candies[i][j-1]
            ans = max(check_col(candies,j-1,i),ans)
            ans = max(check_col(candies,j,i),ans)
            ans = max(check_row(candies,j-1,i),ans)
            ans = max(check_row(candies,j,i),ans)
            candies[i][j],candies[i][j-1] = candies[i][j-1],candies[i][j]
            ans = max(check_col(candies,j-1,i),ans)
            ans = max(check_col(candies,j,i),ans)
            ans = max(check_row(candies,j-1,i),ans)
            ans = max(check_row(candies,j,i),ans)

        if i > 0:
            candies[i-1][j],candies[i][j] = candies[i][j],candies[i-1][j]
            ans = max(check_col(candies,j,i-1),ans)
            ans = max(check_col(candies,j,i),ans)
            ans = max(check_row(candies,j,i-1),ans)
            ans = max(check_row(candies,j,i),ans)
            candies[i][j],candies[i-1][j] = candies[i-1][j],candies[i][j]
            ans = max(check_col(candies,j,i-1),ans)
            ans = max(check_col(candies,j,i),ans)
            ans = max(check_row(candies,j,i-1),ans)
            ans = max(check_row(candies,j,i),ans)

print(ans)

'''
3
PCP
CCP
PCZ

# 출력
2
# 정답
3
'''