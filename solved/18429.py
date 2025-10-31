# from sys import stdin   
# from itertools import permutations as perm

# N,K = map(int,stdin.readline().strip().split())
# A = [i-K for i in map(int,stdin.readline().strip().split())]
# ans = 0
# for i in perm(A,N):
#     tmp = 0
#     for j in i:
#         tmp+=j
#         if tmp < 0:
#             break
#     else:
#         ans+=1

# print(ans)

from sys import stdin  

N,K = map(int,stdin.readline().strip().split())
A = list(map(int,stdin.readline().strip().split()))
visited = [False]*N
ans = 0

def solution(n=0,val=500):
    global ans,N,K,visited
    if n == N:
        ans+=1
        return
    
    for i in range(N):
        if not visited[i]:            
            if val - K + A[i] >= 500:
                visited[i] = True
                solution(n+1,val - K + A[i])
                visited[i] = False

solution()
print(ans)
