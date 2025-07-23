from sys import stdin   
from heapq import heappush,heappop

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    k = int(stdin.readline().strip())

    h_max,h_min = [],[]
    max_stack,min_stack = {},{}

    for _ in range(k):
        order,number = stdin.readline().strip().split()
        if order == 'I':
            heappush(h_max,-int(number))
            heappush(h_min,int(number))

        elif order == 'D' and number == '1':
            while h_max:
                v = -heappop(h_max)
                if max_stack.get(v):
                    max_stack[v]-=1
                else:
                    break
            else:
                continue

            if not min_stack.get(v):
                min_stack.update({v:0})
            min_stack[v]+=1

        elif order == 'D' and number == '-1':
            while h_min:
                v = heappop(h_min)
                if min_stack.get(v):
                    min_stack[v]-=1
                else:
                    break
            else:
                continue

            if not max_stack.get(v):
                max_stack.update({v:0})
            max_stack[v]+=1

    if len(h_min) > sum(min_stack.values()):

        while h_min:
            vmin = heappop(h_min)
            if min_stack.get(vmin):
                min_stack[vmin]-=1
            else:
                break

        while h_max:
            vmax = -heappop(h_max)
            if max_stack.get(vmax):
                max_stack[vmax]-=1
            else:
                break
        
        ans.append([vmax,vmin])
    else:
        ans.append(['EMPTY'])

for i in ans:
    print(*i)
