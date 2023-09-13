from sys import stdin 

N = int(stdin.readline().strip())
cows_loc = dict()
answer = 0
for _ in range(N):
    cow_num,move = map(int,stdin.readline().strip().split())
    if cow_num in cows_loc.keys():
        if cows_loc[cow_num] != move:
            answer+=1
            cows_loc[cow_num] = move
    else:
        cows_loc.update({cow_num:move})

print(answer)
