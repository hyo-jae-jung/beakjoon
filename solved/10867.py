from sys import stdin 
N = int(stdin.readline().strip())
A = [int(i) for i in stdin.readline().strip().split()]

answer = set()

while A:
    temp = A.pop()
    if temp not in answer:
        answer.add(temp)

answer = sorted(list(answer))
print(*answer)
