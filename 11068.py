from sys import stdin 



def check_notation(n:int,B:int) -> str:
    tmp = ''
    while n:
        tmp = str(n%B) + tmp
        n//B
    return tmp

def check_decalcomanie(x):
    l = len(x)//2 + (1 if len(x)%2 else 0)
    i = 0
    while i < l:
        if x[i] == x[-(i+1)]:
            i+=1
        else:
            return False        
    return True

def solution(x):
    for i in range(2,65):
        if check_decalcomanie(check_notation(x,i)):
            return 1
    return 0

# T = int(stdin.readline().strip())
# ans = []
# for _ in range(T):
#     num = int(stdin.readline().strip())
#     ans.append(solution(num))
    
# print(*ans,sep='\n')

print(check_decalcomanie('123421'))