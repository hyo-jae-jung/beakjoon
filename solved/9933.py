from sys import stdin 

N = int(stdin.readline().strip())
words = []
for _ in range(N):
    words.append(stdin.readline().strip())

answer = ''

for i in words:
    if ''.join(reversed(i)) in words:
        answer = i
        break

word_length = len(answer)

print(word_length,answer[word_length//2])
