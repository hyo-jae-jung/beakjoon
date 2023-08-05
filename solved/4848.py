from sys import stdin 

T = int(stdin.readline().strip())

def cnt(s):
    cnt=0
    while s[-1*(cnt+2)] == '}':
        cnt+=1
    return cnt

arr = ['{}'] + [False]*15

def dp(n):
    if arr[n]:
        return arr[n]
    
    for i in range(n):
        tmp = arr[i][1:-1]
        arr[i+1] = '{'+((tmp+',') if tmp else '') + arr[i] + '}'
    return arr[n]

answer = []

for _ in range(T):
    a = stdin.readline().strip()
    b = stdin.readline().strip()
    a_num,b_num = cnt(a),cnt(b)

    answer.append(dp(a_num+b_num))

print(*answer,sep='\n')
