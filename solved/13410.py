from sys import stdin 

N,K = map(int,stdin.readline().strip().split())

l = []
for i in range(1,K+1):
    l.append(int(''.join(list(reversed(str(N*i))))))

print(max(l))
