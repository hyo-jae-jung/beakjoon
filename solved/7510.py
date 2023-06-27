from heapq import heappop,heapify

n = int(input())

answer = []
for _ in range(n):
    temp = list(map(int,input().split()))
    heapify(temp)
    a = heappop(temp)
    b = heappop(temp)
    c = heappop(temp)
    answer.append('yes' if a**2+b**2 == c**2 else 'no')

for i,j in enumerate(answer,1):
    print(f"Scenario #{i}:",j,'',sep='\n')
    
