from sys import stdin 

S,K,H = map(int,stdin.readline().strip().split())

if S+K+H >= 100:
    print("OK")
else:
    l = sorted([("Soongsil",S),("Korea",K),("Hanyang",H)],key=lambda x:(x[1]))
    print(l[0][0])
