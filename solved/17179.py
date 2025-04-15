from sys import stdin  

N,M,L = map(int,stdin.readline().strip().split())
cut_points = []
for _ in range(M):
    cut_points.append(int(stdin.readline().strip()))

cut_points.sort()

friend_list = []
for _ in range(N):
    friend_list.append(int(stdin.readline().strip()))

def binary_search(x):
    left = 0
    right = L
    
    while left < right:
        mid = (left+right)//2 + (1 if (left+right)%2 > 0 else 0)
        piece = 0
        loc = 0
        size = L
        a = []
        for i in cut_points:
            if i - loc >= mid:
                a.append(i-loc)
                size = min(size,i-loc)
                piece+=1
                loc = i
        else:
            if L-loc >= mid:
                a.append(L-loc)
                size = min(size,L - loc)
            else:
                a[-1]+=L-loc
                piece-=1

        if piece >= x:
            left = mid
        else:
            right = mid - 1
    
    return left

for i in friend_list:
    print(binary_search(i))
