from sys import stdin  
from copy import deepcopy

direction = [(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1)]
dataset = {
    'graph':[[0]*4 for _ in range(4)],
    'fish_info':{},
    'shark_info':{},
}
tmp = [list(map(int,stdin.readline().strip().split())) for _ in range(4)]

result = 0  

for i in range(4):
    for j in range(8):
        if j%2 == 0:
            dataset['graph'][i][j//2] = tmp[i][j]
        else:
            dataset['fish_info'].update({tmp[i][j-1]:[i,j//2,tmp[i][j]%8]})

def shark_move(dataset):
    ans = []
    if not dataset['shark_info']:
        feed_fish_num = dataset['graph'][0][0]
        dataset['shark_info'].update({'shark_loc':(0,0),
                                      'shark_direction':dataset['fish_info'][feed_fish_num][2],
                                      'shark_feed_sum' : feed_fish_num,
                                      })
        
        del dataset['fish_info'][feed_fish_num]
        dataset['graph'][0][0] = 100
        ans.append(dataset)
        return ans
    
    dy,dx = direction[dataset['shark_info']['shark_direction']]
    y,x = dataset['shark_info']['shark_loc']
    for i in range(1,4):
        if 0 <= (nx:=x+dx*i) < 4 and 0 <= (ny:=y+dy*i) < 4:
            if 1 <= dataset['graph'][ny][nx] <= 16:
                c_dataset = deepcopy(dataset)
                feed_fish_num = c_dataset['graph'][ny][nx]
                feed_fish_direction = c_dataset['fish_info'][feed_fish_num][2]
                c_dataset['shark_info']['shark_direction'] = feed_fish_direction
                c_dataset['shark_info']['shark_feed_sum']+=feed_fish_num
                y,x = c_dataset['shark_info']['shark_loc']
                c_dataset['graph'][ny][nx] = 100
                c_dataset['graph'][y][x] = -1
                c_dataset['shark_info']['shark_loc'] = (ny,nx)
                del c_dataset['fish_info'][feed_fish_num]
                ans.append(c_dataset)
                del c_dataset
    if not ans:
        global result
        result = max(result,dataset['shark_info']['shark_feed_sum'])

    return ans

def fish_move(dataset):
    for i in range(1,17):
        if dataset['fish_info'].get(i):
            y = dataset['fish_info'][i][0]
            x = dataset['fish_info'][i][1]
            d = dataset['fish_info'][i][2]

            while True:
                dy,dx = direction[d]
                nx = x+dx
                ny = y+dy
                if 0 > nx or nx >= 4 or 0 > ny or ny >= 4 or dataset['graph'][ny][nx] == 100:
                    d = (d+1)%8
                else:
                    break  

            dataset['fish_info'][i][2] = d
            dy,dx = direction[d]

            target = dataset['graph'][(ny:=y+dy)][(nx:=x+dx)]

            if dataset['fish_info'].get(target):
                dataset['fish_info'][target][0] = y
                dataset['fish_info'][target][1] = x

            dataset['fish_info'][i][0] = ny
            dataset['fish_info'][i][1] = nx

            dataset['graph'][y][x],dataset['graph'][ny][nx] = dataset['graph'][ny][nx],dataset['graph'][y][x]

    return dataset

D = []
D = shark_move(dataset)

while D:
    tmp_dataset = D.pop()
    tmp_dataset = fish_move(tmp_dataset)
    D.extend(shark_move(tmp_dataset))

print(result)
