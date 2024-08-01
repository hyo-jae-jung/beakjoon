from sys import stdin  

ps = list(map(int,stdin.readline().strip().split()))
x,y,r = map(int,stdin.readline().strip().split())

if x in ps:
    print(ps.index(x)+1)
else:
    print(0)
    