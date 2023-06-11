import sys
sys.setrecursionlimit(10**4)

N,M = map(int,sys.stdin.readline().strip().split())

iceberg = []
for _ in range(N):
    iceberg.append(list(map(int,sys.stdin.readline().strip().split())))


def check_iceberg_cnt(arr):

    arr = [i.copy() for i in arr]

    def dfs(x,y):
        if x < 0 or y < 0 or x >= M or y >= N:
            return False
        
        if arr[y][x] > 0:
            arr[y][x] = 0
            dfs(x-1,y)
            dfs(x+1,y)
            dfs(x,y-1)
            dfs(x,y+1)
            return True
    
    answer = 0

    for i in range(N):
        for j in range(M):
            if dfs(j,i) == True:
                answer+=1

    return answer

def iceberg_diff_by_years(arr):
    new_arr = [[0]*M for _ in range(N)]

    def check_all_directions(x,y):
        answer = 0
        if arr[y][x] != 0:
            if x-1 >= 0 and y >= 0 and x-1 < M and y < N:
                if arr[y][x-1] == 0:
                    answer+=1
            if x+1 >= 0 and y >= 0 and x+1 < M and y < N:
                if arr[y][x+1] == 0:
                    answer+=1
            if x >= 0 and y-1 >= 0 and x < M and y-1 < N:
                if arr[y-1][x] == 0:
                    answer+=1
            if x >= 0 and y+1 >= 0 and x < M and y+1 < N:
                if arr[y+1][x] == 0:
                    answer+=1
        return answer

    for i in range(N):
        for j in range(M):
            new_arr[i][j] = check_all_directions(j,i)

    return new_arr

answer = 0

while check_iceberg_cnt(iceberg) == 1:

    diff = iceberg_diff_by_years(iceberg)

    for i in range(N):
        for j in range(M):
            temp = iceberg[i][j] - diff[i][j]
            iceberg[i][j] = temp if temp >= 0 else 0

    answer+=1

    if sum(sum(iceberg,[])) == 0:
        print(0)
        break
else:
    print(answer)
