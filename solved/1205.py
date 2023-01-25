from bisect import bisect_right  
from sys import stdin 

N,new_score,P = map(int,stdin.readline().strip().split())
if N == 0:
    print(1)
else:
    scores = [int(i) for i in stdin.readline().strip().split()]
    scores.sort()
    l = len(scores)
    if l >= P:
        if scores[l-P] >= new_score:
            print(-1)
        else:
            print(l-bisect_right(scores,new_score)+1)
    else:
        print(l-bisect_right(scores,new_score)+1)

