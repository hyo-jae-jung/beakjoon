from sys import stdin    

N = int(stdin.readline().strip())
ans = []

def is_prime(n):
    if n in [0,1]:
        return False
    
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
        
    return True

def solution(val='',cnt=0):
    global N,ans
    if cnt == N:
        ans.append(int(val))
        return 
    

    for i in range(10):
        tmp = val+str(i)
        if is_prime(int(tmp)):
            solution(tmp,cnt+1)

solution()
print(*sorted(ans),sep='\n')
