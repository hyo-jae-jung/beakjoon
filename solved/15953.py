from sys import stdin 

T = int(stdin.readline().strip())

reward_a = [500,300,200,50,30,10]
reward_b = [512,256,128,64,32]
max_cnt_a = [1,2,3,4,5,6]
max_cnt_b = [1,2,4,8,16]

def accum(l:list) -> list:
    accum = [l[0]]
    for i in range(1,len(l)):
        accum.append(accum[i-1]+l[i])
    return accum

accum_a = accum(max_cnt_a)
accum_b = accum(max_cnt_b)

ans = []
for _ in range(T):
    a,b = map(int,stdin.readline().strip().split())
    reward_total = 0
    if a:
        for i in range(6):
            if a <= accum_a[i]:
                reward_total+=reward_a[i]
                break
    if b:
        for i in range(5):
            if b <= accum_b[i]:
                reward_total+=reward_b[i]
                break

    reward_total*=10000
    ans.append(reward_total)

print(*ans,sep='\n')
