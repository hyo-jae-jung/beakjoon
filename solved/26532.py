from sys import stdin  

a,b = map(int,stdin.readline().strip().split())
ans = (a*b/4840)/5
print(int(ans) if ans == int(ans) else int(ans) + 1)
