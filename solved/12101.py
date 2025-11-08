from sys import stdin   

n,k = map(int,stdin.readline().strip().split())
ans = -1
seq = 0
def solution(val='0'):
    global n,k,ans,seq
    if val and eval(val) == n:
        seq+=1
        if seq == k:
            ans = val[2:]
        return
    
    if seq < k and eval(val) < n:
        for i in range(1,4):
            solution(val+'+'+str(i))

solution()
print(ans)
