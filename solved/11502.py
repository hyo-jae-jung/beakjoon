arr = [0]*1001
for i in range(2,1001):
    for j in range(2*i,1001,i):
        arr[j]+=1

prime_numbers = []
for i in range(2,1001):
    if arr[i] == 0:
        prime_numbers.append(i)

def solution(k,cnt=0,idx=0,val=0):

    global tmp,ans,b
    if cnt == 3:
        if k == val:
            ans.pop()
            ans.append(' '.join(map(str,tmp)))
            b = False
        return
    
    if b:
        for i in range(idx,len(prime_numbers)):
            if val+prime_numbers[i] <= k:
                tmp.append(prime_numbers[i])
                solution(k,cnt+1,i,val+prime_numbers[i])
                tmp.pop()
            else:
                break

import sys

T = int(sys.stdin.readline().strip())
ans = []
for _ in range(T):
    ans.append(0)
    K = int(sys.stdin.readline().strip())
    tmp = []
    b = True
    solution(K)

for i in ans:
    print(i)
