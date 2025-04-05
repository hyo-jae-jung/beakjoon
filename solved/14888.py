from sys import stdin   

N = int(stdin.readline().strip())
nums = list(map(int,stdin.readline().strip().split()))
operators = list(map(int,stdin.readline().strip().split()))
ans = []

def solution(operators,i=1,val=nums[0]):
    
    global N,ans
    if i == N:
        ans.append(val)
        return True
    
    operators2 = operators.copy()

    global nums
    if operators2[0]:
        operators2[0]-=1
        solution(operators2,i=i+1,val=val+nums[i])
        operators2[0]+=1

    if operators2[1]:
        operators2[1]-=1
        solution(operators2,i=i+1,val=val-nums[i])
        operators2[1]+=1

    if operators2[2]:
        operators2[2]-=1
        solution(operators2,i=i+1,val=val*nums[i])
        operators2[2]+=1

    if operators2[3]:
        operators2[3]-=1
        solution(operators2,i=i+1,val=val//nums[i] if val >= 0 else -1*(abs(val)//nums[i]))

solution(operators=operators)    

ans.sort()
print(ans[-1])
print(ans[0])
