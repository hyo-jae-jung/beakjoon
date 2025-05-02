from sys import stdin 

N = int(stdin.readline().strip())
balloon = list(enumerate(map(int,stdin.readline().strip().split()),1))

ans = []
loc = 0
while N > 0:
    idx,div = balloon[loc]
    ans.append(idx)
    
    new_loc = loc+div
    if new_loc > loc:
        new_loc-=1
    N-=1
    new_loc = 0 if N == 0 else new_loc%N

    new_balloon = []
    for i,j in enumerate(balloon):
        if i != loc:
            new_balloon.append(j)
    balloon = new_balloon.copy()

    loc = new_loc - (1 if new_loc == len(balloon) else 0)

print(*ans)
