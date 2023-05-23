from sys import stdin 

n = int(stdin.readline().strip())
H = [int(i) for i in stdin.readline().strip().split()]
A = [int(i) for i in stdin.readline().strip().split()]

ha = []
for i,j in zip(H,A):
    ha.append((i,j))

ha.sort(key=lambda x:x[1])

answer = 0
for i in range(n):
    answer+=ha[i][0]+ha[i][1]*i

print(answer)
