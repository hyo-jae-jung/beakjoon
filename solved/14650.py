from sys import stdin   

N = int(stdin.readline().strip())

ans = 0
def solution(cnt=N,val=''):
    global ans
    if cnt == 0:
        if int(val)%3 == 0:
            ans+=1
        return 
    
    for i in ['0','1','2']:
        solution(cnt-1,val+i)

solution(N-1,'1')
solution(N-1,'2')
print(ans)
