from sys import stdin  

N,K = map(int,stdin.readline().strip().split())
C = list(map(int,stdin.readline().strip().split()))

dp = [0] + [N+1]*K
for i in C:
    for j in range(i,K+1):
        dp[j] = min(dp[j],dp[j-i]+1)

print(dp[-1] if dp[-1] <= N else -1)

"""
문제의 답은 최소 커피 개수이다.
그래서 
최소값 구하기어서 초기값을 가질 수 있는 값의 최대값보다 큰 값을 입력했는데
결과값이 커피 개수이기 때문에 각 원소의 초기값을 주어진 개수+1개로 설정
개수이기 때문에 배낭 크기에 해당하는 값은 모두 1

O(N^2)로 계산
"""
