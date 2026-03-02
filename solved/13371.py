def sn(i,a):
    return a*i*(i+1)//2

from sys import stdin 

T = int(stdin.readline().strip())
ans = []

for _ in range(T):
    n = int(stdin.readline().strip())

    left,right = 0,n
    while left < right:
        mid = (left+right)//2
        if sn(mid,3) < n:
            left = mid + 1
        else:
            right = mid

    in_lev_val = n - sn(right-1,3)
    result:str

    if 0 < in_lev_val <= 1*right:
        result = str(right) + " dolphin" + ("s" if right > 1 else "")
    elif 1*right < in_lev_val <= 2*right:
        result = str(right) + " jump" + ("s" if right > 1 else "")
    elif 2*right < in_lev_val <= 3*right:
        result = "splash"

    ans.append(result)

print(*ans,sep='\n')
