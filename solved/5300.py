from sys import stdin  

N = int(stdin.readline().strip())

ans = []

for i in range(1,N+1):
    ans.append(i)
    if i%6 == 0:
        ans.append('Go!')

else:
    if ans[-1] != 'Go!':
        ans.append('Go!')

print(*ans)
