from sys import stdin 

def check_seq(a:tuple,b:tuple)->int:
    for i in range(3):
        if a[i] > b[i]:return 0
        elif a[i] < b[i]:return 1
    else:
        return 0
    
answer = 1
N,K = map(int,stdin.readline().strip().split())
d = dict()

for _ in range(N):
    seq,G,S,B = map(int,stdin.readline().strip().split())
    d.update({seq:(G,S,B)})

for i in range(1,N+1):
    answer+=check_seq(d[K],d[i])

print(answer)
