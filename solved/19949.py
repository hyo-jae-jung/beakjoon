from sys import stdin    

answer = list(map(int,stdin.readline().strip().split()))
ans = 0

def solution(val='',cnt=0):
    global answer, ans

    if 10 - len(val) + cnt < 5:
        return

    if len(val) == 10:
        if cnt >= 5:
            ans+=1
        return 
    
    for i in range(1,6):
        if len(val) <= 1 or val[-1] != val[-2] or val[-1] != str(i):
            solution(val+str(i),cnt+(0 if i != answer[len(val)] else 1))

solution()
print(ans)
