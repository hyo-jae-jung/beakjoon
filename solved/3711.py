from sys import stdin  

N = int(stdin.readline().strip())
ans = []
for _ in range(N):
    G = int(stdin.readline().strip())
    nums = []
    for _ in range(G):
        nums.append(int(stdin.readline().strip()))

    i = 1
    while G != len(set([j%i for j in nums])):
        i+=1

    ans.append(i)

print(*ans,sep='\n')
