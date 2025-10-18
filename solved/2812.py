from sys import stdin  

N,K = map(int,stdin.readline().strip().split())
nums = stdin.readline().strip()

stack = []
for num in nums:
    
    while stack and K > 0 and stack[-1] < int(num):
        stack.pop()
        K-=1

    stack.append(int(num))

l = list(map(str,stack))
for _ in range(K):
    l.pop()
    
print(''.join(l))
