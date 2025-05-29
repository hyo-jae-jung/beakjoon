from sys import stdin

N = int(stdin.readline().strip())

dp = [0]*(N+1)

for i in range(2,N+1):
    dp[i] = dp[i-1] + 1
    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i%3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[-1])

"""
2년 전에 풀었던 아래의 방법이 시간복잡도와 공간복잡도 모두 효율적이다.
"""

# from collections import deque, defaultdict 
# queue = deque([[N,0]])
# answer = 0

# memo = defaultdict(bool)

# while queue:
    
#     temp = queue.popleft()

#     if temp[0] == 1:
#         answer = temp[1]
#         break

#     if temp[0]%2 == 0:
#         loc = temp[0]//2
#         if not memo[loc]:
#             queue.append([loc,temp[1]+1])
#             memo[loc] = True

#     if temp[0]%3 == 0:
#         loc = temp[0]//3
#         if not memo[loc]:
#             queue.append([loc,temp[1]+1])
#             memo[loc] = True

#     if temp[0] > 1:
#         loc = temp[0]-1
#         if not memo[loc]:
#             queue.append([loc,temp[1]+1])
#             memo[loc] = True

# print(answer)
