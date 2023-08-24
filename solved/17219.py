from sys import stdin 

N,M = map(int,stdin.readline().strip().split())

accounts = dict()
for _ in range(N):
    uri,password = stdin.readline().strip().split()
    accounts.update({uri:password})

answer = []
for _ in range(M):
    answer.append(accounts[stdin.readline().strip()])

print(*answer,sep='\n')

