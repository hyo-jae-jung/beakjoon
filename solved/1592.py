from sys import stdin 

N,M,L = map(int,stdin.readline().strip().split())

ans = 0
people = [1] + [0]*(N-1)
i = 0
while max(people) < M:
    if people[i]%2 == 0:
        people[(i-L)%N]+=1
        i = (i-L)%N
    else:
        people[(i+L)%N]+=1
        i = (i+L)%N
    ans+=1

print(ans)
