from sys import stdin  

N = int(stdin.readline().strip())

while (set(str(N))|set(['4','7'])) != set(['4','7']):
    N-=1

print(N)
