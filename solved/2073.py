from sys import stdin  

D,P = map(int,stdin.readline().strip().split())
items = [tuple(map(int,stdin.readline().strip().split())) for _ in range(P)]

dp = [2**23] + [0]*D
for l,c in items:
    for i in range(D,l-1,-1):
        dp[i] = max(dp[i],min(dp[i-l],c))

print(dp[-1])

"""
최대값을 구하는 문제여서 두 번째 for문을 역순으로 설정
연산과정에 min이 있지만 본질은 변하지 않음
"""
