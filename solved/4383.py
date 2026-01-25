from sys import stdin  

e = stdin.read().strip()
lines = e.splitlines()
ans = []

for i in lines:
    arr = list(map(int,i.split()))
    l = int(arr[0])
    arr = arr[1:].copy()
    result = "Not jolly"
    if l > 0:
        bitmask = 2**(l-1) - 1
        for i in range(1,l):
            tmp = abs(arr[i] - arr[i-1])-1
            if 0 <= tmp < l:
                bin_k = 1 << tmp
                if bin_k & bitmask == bin_k:
                    bitmask-=bin_k
        else:
            if bitmask == 0:
                result = "Jolly"

    ans.append(result)

print(*ans,sep='\n')
