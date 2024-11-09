from sys import stdin  

ans = []
def solution(S):
        s,t = S.split()
        tmp = ''
        for i in t:
            if i in s:
                tmp+=i
        if s in tmp:
            return 'Yes'
        else:
            return 'No'

while True:
    try:
        ans.append(solution(stdin.readline().strip()))
    except:
         break

print(*ans,sep='\n')
