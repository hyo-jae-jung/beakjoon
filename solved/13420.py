from sys import stdin  

T = int(stdin.readline().strip())
ans = []
for _ in range(T):
    left,right = stdin.readline().strip().split('=')
    if eval(left) == int(right):
        ans.append("correct")
    else:
        ans.append("wrong answer")

print(*ans,sep='\n')
