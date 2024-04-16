from sys import stdin 

N = int(stdin.readline().strip())

success = []
for _ in range(N):
    t1,t2 = stdin.readline().strip().split()
    if int(t1) <= int(t2):
        success.append(int(t2))

print(min(success) if success else -1)
