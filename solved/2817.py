from sys import stdin   
from heapq import heapify,heappop

X = int(stdin.readline().strip())
N = int(stdin.readline().strip())
scores = {}
coins = {}
for _ in range(N):
    staff,score = stdin.readline().strip().split()
    a,b = int(0.05*X),1 if (0.05*X)%1 > 0 else 0
    if int(score) >= a+b:
        scores.update({staff:int(score)*360360})
        coins.update({staff:0})
        
arr = []
for k in range(1,15):
    arr+=[(-j//k,i) for i,j in scores.items()]
    
heapify(arr)

for _ in range(14):
    _,staff = heappop(arr)    
    coins[staff]+=1

for i in sorted(coins.items(),key=lambda x:x[0]):
    print(*i)
