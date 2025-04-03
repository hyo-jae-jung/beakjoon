from sys import stdin  

T = int(stdin.readline().strip())
ans = []

def solution(t='1',v='1',i=1):

    global N
    if i == N:
        if eval(v) == 0:
            tmp.append(t)
        return True
    
    global nums
    if eval(v) > int(nums[i:]):
        return False
    
    solution(t=t+f'+{nums[i]}',v=v+f'+{nums[i]}',i=i+1)
    solution(t=t+f'-{nums[i]}',v=v+f'-{nums[i]}',i=i+1)
    solution(t=t+f' {nums[i]}',v=v+f'{nums[i]}',i=i+1)

for _ in range(T):
    N = int(stdin.readline().strip())
    nums = ''.join(map(str,range(1,N+1)))
    tmp = []
    solution()
    ans.append('')
    ans.extend(sorted(tmp))

for i in ans[1:]:
    print(i)
