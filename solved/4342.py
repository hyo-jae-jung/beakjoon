from sys import stdin  

ANS = []

def solution(a,b):
    j = 0
    ans = ['A wins','B wins']
    arr = []
    while b > 0:
        c = a//b
        d = a - b*c
        a = b
        b = d 
        if c > 1:
            arr.append(2)
        else:
            arr.append(1)

    arr.pop()
    for i in arr:
        if i == 2:
            return ans[j%2]
        else:
            j+=1
    else:
        return ans[j%2]

while (t := stdin.readline().strip()) != '0 0':
    a,b = map(int,t.split())
    A,B = max(a,b), min(a,b)
    ANS.append(solution(A,B))

print(*ANS,sep='\n')
