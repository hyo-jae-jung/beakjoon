from sys import stdin 

K = int(stdin.readline().strip())
min_chocolate = 1
min_break = 0
n = 0
while (min_chocolate := 2**n) < K:
    n+=1

if min_chocolate == K:
    print(K,0)
    
else:
    reduce_chocolate = min_chocolate
    m = 1
    while (min_break := min_break + (reduce_chocolate := (reduce_chocolate//2 if reduce_chocolate//2 > 0 else 1))) != K:
        m+=1
        if min_break > K:
            min_break-=reduce_chocolate

    print(min_chocolate,m)
