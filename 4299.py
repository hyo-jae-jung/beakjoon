from sys import stdin  

a,b = map(int,stdin.readline().strip().split())
a,b = max(a,b),min(a,b)
print((str((a+b)//2) + ' ' + str((a-b)//2)) if (a+b)//2 == (a+b)/2 and (a-b)//2 == (a-b)/2 else -1)
