N = int(input())
M = [input() for _ in range(N)]

answer = []

for i in M:
    temp = []
    for j in i.split():
        temp.append(''.join(reversed(j)))
    print(' '.join(temp))
