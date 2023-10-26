from sys import stdin 

_,_ = stdin.readline().strip().split()
A = set(map(int,stdin.readline().strip().split()))
B = set(map(int,stdin.readline().strip().split()))
ans = A-B
print(len(ans))
if ans:
    print(*sorted(list(ans)))
