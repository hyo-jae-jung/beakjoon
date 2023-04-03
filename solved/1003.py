from sys import stdin

T = int(stdin.readline().strip())

inp = []

box = []
box.append((1,0))
box.append((0,1))

def fibonacci(n):
    try:
        return box[n]
    except:
        pass
    
    start_idx = len(box)-1
    while (start_idx:=start_idx+1) <= n:
        box.append((box[start_idx-1][0]+box[start_idx-2][0],box[start_idx-1][1]+box[start_idx-2][1]))
    return box[start_idx-1]

for _ in range(T):
    inp.append(int(stdin.readline().strip()))
    
for i in inp:
    print(*fibonacci(i))
    