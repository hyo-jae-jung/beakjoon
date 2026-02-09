from sys import stdin 

N = int(stdin.readline().strip())
count_1 = [0]*20
for _ in range(N):
    name = int(stdin.readline().strip())
    for i in range(20):
        if name >= (1 << i):
            if name & (1 << i) > 0:
                count_1[i]+=1
        else:
            break

ans = 0
for i in range(20):
    ans+=(1 << i)*count_1[i]*(N-count_1[i])

print(ans)
