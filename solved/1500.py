from sys import stdin 

S,K = map(int,stdin.readline().strip().split())
answer = 1
P = S//K+1
while S%K:
    answer*=P
    S-=P
    K-=1
else:
    answer*=(S//K)**K

print(answer)
