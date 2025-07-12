def game(arr):
    while (l:=len(arr)) > 2:
        tmp = []
        for i in range(l//2 + (1 if l%2 > 0 else 0)):
            tmp.append(arr[i]+arr[-(i+1)])
        arr = tmp
    if arr[0] > arr[1]:
        return "Alice"
    else:
        return "Bob"

from sys import stdin   

T = int(stdin.readline().strip())
ans = []
for i in range(1,T+1):
    N = int(stdin.readline().strip())
    arr = list(map(int,stdin.readline().strip().split()))
    ans.append(f"Case #{i}: {game(arr)}")

print(*ans,sep='\n')
