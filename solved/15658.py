from sys import stdin   

N = int(stdin.readline().strip())
A = list(map(int,stdin.readline().strip().split()))
F = list(map(int,stdin.readline().strip().split()))

ans_max = -float('inf')
ans_min = float('inf')

def solution(n=0,val=0):
    global N,A,F,ans_max,ans_min
    if n == N:
        ans_max = max(ans_max,val)
        ans_min = min(ans_min,val)
        return 
    
    if n == 0:
        solution(n+1,val+A[n])
        return
    
    for i in range(4):
        if F[i] > 0:
            F[i]-=1
            if i == 0:
                solution(n+1,val+A[n])
            elif i == 1:
                solution(n+1,val-A[n])
            elif i == 2:
                solution(n+1,val*A[n])
            else:
                if val < 0:
                    solution(n+1,-1*((-1*val)//A[n]))
                else:
                    solution(n+1,val//A[n])
            F[i]+=1

solution()
print(ans_max)
print(ans_min)
