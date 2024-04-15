from sys import stdin 

N = int(stdin.readline().strip())
monitor = []
for i in range(1,N+1):
    W,H = map(int,stdin.readline().strip().split())
    monitor.append((((W**2+H**2)**0.5)/77,i))

for _,j in sorted(monitor,key=lambda x:(-x[0],x[1])):
    print(j)
