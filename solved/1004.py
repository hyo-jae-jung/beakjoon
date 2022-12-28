import sys

T = int(sys.stdin.readline().strip())

def pass_cnt(fe:list,i,j,k)->int:
    cnt = 0
    if any([all([(fe[0]-i)**2 + (fe[1]-j)**2 > k**2,(fe[2]-i)**2 + (fe[3]-j)**2 < k**2]),all([(fe[0]-i)**2 + (fe[1]-j)**2 < k**2,(fe[2]-i)**2 + (fe[3]-j)**2 > k**2])]):
        cnt+=1
    return cnt

cnt_list = []
for _ in range(T):
    cnt = 0
    fe = list(map(int,sys.stdin.readline().strip().split()))
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        i,j,k = map(int,sys.stdin.readline().strip().split())
        cnt+= pass_cnt(fe,i,j,k)
    cnt_list.append(cnt)

for i in cnt_list:
    print(i)

# if __name__ == "__main__":
#     print(pass_cnt([-5,1,12,1],1,1,8))
