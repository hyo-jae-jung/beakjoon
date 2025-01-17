from sys import stdin  

rest_patty,rest_cheese = map(int,stdin.readline().strip().split())

patty,rest_patty = rest_patty//2,rest_patty%2

if patty > rest_cheese:
    cheese = rest_cheese
    rest_cheese = 0
    rest_patty+=(patty-cheese)*2
    patty-=(patty-cheese)
else:
    cheese = patty
    rest_cheese-=patty

double_burger_cnt = 0

while rest_patty > 0 or rest_cheese > 0:
    patty-=1
    rest_patty+=2
    cheese-=1
    rest_cheese+=1
    if rest_cheese == rest_patty:
        double_burger_cnt = rest_patty
        break
    if patty == 0:
        break

if patty == 0:
    print('NO')
else:
    print('YES')
    print(patty)
    for _ in range(patty):
        if double_burger_cnt > 0:
            print('aba'+'ba'*double_burger_cnt)
            double_burger_cnt = 0
        else:
            print('aba')
