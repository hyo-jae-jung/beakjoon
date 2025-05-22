from sys import stdin  

N = int(stdin.readline().strip())
table = [0]*101
for i in range(1,10):
    for j in range(1,10):
        table[i*j] = 1

print(table[N])
