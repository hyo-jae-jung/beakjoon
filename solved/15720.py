from sys import stdin 

B,C,D = map(int,stdin.readline().strip().split())
bugger = list(map(int,stdin.readline().strip().split()))
side_menu = list(map(int,stdin.readline().strip().split()))
beverage = list(map(int,stdin.readline().strip().split()))
print(sum([*bugger,*side_menu,*beverage]))

answer = 0
bugger.sort()
side_menu.sort()
beverage.sort()

min_BCD = min(B,C,D)

for i,j in enumerate(range(max(B,C,D))):
    b_tmp,s_tmp,v_tmp,rate = 0,0,0,1
    if bugger:
        b_tmp = bugger.pop()
    if side_menu:
        s_tmp = side_menu.pop()
    if beverage:
        v_tmp = beverage.pop()
    if i < min_BCD:
        rate = 0.9
    answer+=(b_tmp+s_tmp+v_tmp)*rate

print(int(answer))
