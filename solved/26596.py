from sys import stdin  
from itertools import combinations as comb

M = int(stdin.readline().strip())
bottle = {}
ans = "Not Delicious..."
for _ in range(M):
    liquid,volume = stdin.readline().strip().split()
    if not bottle.get(liquid):
        bottle.update({liquid:0})
    bottle[liquid]+=int(volume)
    
cnt = bottle.__len__()
arr = list(bottle.items())
for a,b in comb(range(cnt),2):
    c,d = min(arr[a][1],arr[b][1]),max(arr[a][1],arr[b][1])
    if (c*1.618)//1 == d:
        ans = "Delicious!"
        break

print(ans)
