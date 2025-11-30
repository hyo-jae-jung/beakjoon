from sys import stdin  

nums = stdin.readline().strip()

visited = [True] + [False]*50
ans = []
tmp = []
def solution(idx=0,max_num=0):
    global nums,visited,ans,tmp
    if idx >= len(nums):
        if all(visited[:max_num+1]):
            ans = tmp.copy()
        return 
    
    val = ''
    if not ans:
        val+=nums[idx]
        if not visited[int(val)]:
            visited[int(val)] = True
            tmp.append(val)
            solution(idx+1,max(max_num,int(val)))
            visited[int(val)] = False
            tmp.pop()

        if idx+1 < len(nums):
            val+=nums[idx+1]
            if int(val) <= 50 and not visited[int(val)]:
                visited[int(val)] = True
                tmp.append(val)
                solution(idx+2,max(max_num,int(val)))
                visited[int(val)] = False
                tmp.pop()

solution()
print(*ans)
