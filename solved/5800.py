from sys import stdin 

K = int(stdin.readline().strip())
ans = []
for _ in range(K):
    score = sorted(list(map(int,stdin.readline().strip().split()))[1:])
    first = score[0]
    end = score[-1]
    max_diff = 0
    for i in range(1,len(score)):
        if max_diff < score[i] - score[i-1]:
            max_diff = score[i] - score[i-1]
    
    ans.append((first,end,max_diff))

for i,j in enumerate(ans,1):
    print(f"Class {i}\nMax {j[1]}, Min {j[0]}, Largest gap {j[2]}")
