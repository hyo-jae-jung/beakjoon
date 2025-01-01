from sys import stdin  

N = int(stdin.readline().strip())
weathers = list(map(int,stdin.readline().strip().split()))
state = 0
ans = 0
for i in weathers:
    if i == 1:
        state+=1
    else:
        state-=1
    ans+=state

print(ans)
