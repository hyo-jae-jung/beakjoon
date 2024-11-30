from sys import stdin  

n = int(stdin.readline().strip())
students = sorted(list(map(int,stdin.readline().strip().split())))
ans = 2*10**5
for i in range(n):
    ans = min(ans,students[i]+students[-1*(i+1)])

print(ans)
