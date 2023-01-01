import sys

S = sys.stdin.readline().strip()
answer = []
for i in range(len(S)):
    answer.append(S[i:])

for i in sorted(answer):
    print(i)
