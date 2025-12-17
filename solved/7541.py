from sys import stdin  

scenarios = int(stdin.readline().strip())

def solution(nums:str):
    total = 0
    q_idx = 0
    l = len(nums)
    arr = ['?']*l
    factors = [9,3,7]
    for i in range(1,l+1):
        if nums[-i] != '?':
            arr[-i] = nums[-i]
            total+=int(nums[-i])*factors[(i-1)%3]
            continue

        q_idx = -i
        factor = factors[(i-1)%3]

    for i in range(10):
        result = total+i*factor
        if str(result)[-1] == '0':
            arr[q_idx] = str(i)
            return ''.join(arr)

ans = []
for i in range(1,scenarios+1):
    ans.append(f"Scenario #{i}:")
    ans.append(solution(stdin.readline().strip()))
    ans.append('')

print(*ans,sep='\n')
