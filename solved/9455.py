from sys import stdin 

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    row,column = map(int,stdin.readline().strip().split())
    box,loc = [],[]
    cnt_box_by_col = [0]*column
    move_cnt = 0
    for _ in range(row):
        box.append(stdin.readline().strip().split())

    for i in range(row):
        for j in range(column):
            if box[i][j] == '1':
                loc.append((i,j))
    
    loc.sort(key=lambda x:-x[0])

    for i,j in loc:
        move_cnt+=row-(i+1)-cnt_box_by_col[j]
        cnt_box_by_col[j]+=1

    ans.append(move_cnt)

print(*ans,sep='\n')
