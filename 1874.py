N = int(input())
M = [int(input()) for _ in range(N)]
plus_minus = []
answer = []
for i in range(1,len(M)+1):
    answer.append(i)
    if answer[-1] == M[0]:
        answer.pop()
        M.pop(0)
    print(answer)

print(answer)