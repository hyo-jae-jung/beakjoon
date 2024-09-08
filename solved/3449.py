from sys import stdin  

T = int(stdin.readline().strip())
ans = []

for _ in range(T):
    a = stdin.readline().strip()
    b = stdin.readline().strip()

    cnt = 0

    for i,j in zip(a,b):
        if i != j:
            cnt+=1
    
    ans.append(cnt)

for i in ans:
    print(f"Hamming distance is {i}.")
    